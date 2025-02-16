from fastapi import FastAPI, Form, HTTPException, Depends, Cookie
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Optional, Dict
import jwt
import time

app = FastAPI()
SECRET_KEY = "supersecretkey"
users = []
flowers = []
purchases = []
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_jwt(email: str) -> str:
    payload = {"email": email, "exp": time.time() + 3600}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["email"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Session expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

class User(BaseModel):
    email: str
    name: str
    password: str


class Flower(BaseModel):
    id: int
    name: str
    price: float

class Purchase(BaseModel):
    user_email: str
    flower_id: int

class UsersRepository:
    users: List[User] = []
    @classmethod
    def add_user(cls, user: User):
        cls.users.append(user)
    @classmethod
    def get_user(cls, email: str) -> Optional[User]:
        return next((u for u in cls.users if u.email == email), None)

class FlowersRepository:
    flowers: List[Flower] = []
    @classmethod
    def add_flower(cls, flower: Flower):
        cls.flowers.append(flower)
    @classmethod
    def get_flowers(cls) -> List[Flower]:
        return cls.flowers

class PurchasesRepository:
    purchases: List[Purchase] = []
    @classmethod
    def add_purchase(cls, purchase: Purchase):
        cls.purchases.append(purchase)
    @classmethod
    def get_purchases_by_user(cls, email: str) -> List[Purchase]:
        return [p for p in cls.purchases if p.user_email == email]

@app.post("/signup")
async def signup(email: str = Form(), name: str = Form(), password: str = Form()):
    if UsersRepository.get_user(email):
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    user = User(email=email, name=name, password=password)
    UsersRepository.add_user(user)
    return {"message": "Пользователь зарегистрирован"}

@app.post("/login")
async def login(email: str = Form(), password: str = Form()):
    user = UsersRepository.get_user(email)
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Неверные данные")
    token = create_jwt(email)
    return {"access_token": token, "type": "bearer"}

@app.get("/profile")
async def profile(token: str = Depends(oauth2_scheme)):
    email = decode_jwt(token)
    user = UsersRepository.get_user(email)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"email": user.email, "name": user.name}

@app.get("/flowers")
async def get_flowers():
    return FlowersRepository.get_flowers()

@app.post("/flowers")
async def add_flower(name: str = Form(), price: float = Form()):
    flower_id = len(FlowersRepository.flowers) + 1
    flower = Flower(id=flower_id, name=name, price=price)
    FlowersRepository.add_flower(flower)
    return {"id": flower_id}

@app.post("/cart/items")
async def add_to_cart(flower_id: int = Form(), cart: Optional[str] = Cookie(None)):
    cart_items = cart.split(',') if cart else []
    cart_items.append(str(flower_id))
    response = {"message": "Цветок добавлен в корзину"}
    response["Set-Cookie"] = f"cart={','.join(cart_items)}; Path=/"
    return response

@app.get("/cart/items")
async def view_cart(cart: Optional[str] = Cookie(None)):
    if not cart:
        return {"items": [], "total_price": 0}
    cart_items = cart.split(',')
    cart_flowers = [f for f in FlowersRepository.flowers if str(f.id) in cart_items]
    total_price = sum(f.price for f in cart_flowers)
    return {"items": cart_flowers, "total_price": total_price}

@app.post("/purchased")
async def purchase(token: str = Depends(oauth2_scheme), cart: Optional[str] = Cookie(None)):
    email = decode_jwt(token)
    if not cart:
        raise HTTPException(status_code=400, detail="Корзина пуста")
    cart_items = cart.split(',')
    for flower_id in cart_items:
        PurchasesRepository.add_purchase(Purchase(user_email=email, flower_id=int(flower_id)))
    response = {"message": "Покупка совершена"}
    response["Set-Cookie"] = "cart=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"
    return response

@app.get("/purchased")
async def view_purchases(token: str = Depends(oauth2_scheme)):
    email = decode_jwt(token)
    user_purchases = PurchasesRepository.get_purchases_by_user(email)
    purchased_flowers = [f for f in FlowersRepository.flowers if any(p.flower_id == f.id for p in user_purchases)]
    return {"purchased_flowers": purchased_flowers}
