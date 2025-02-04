from fastapi import FastAPI, Form, Cookie, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List, Optional
import jwt
import time

app = FastAPI()
SECRET_KEY = "supersecretkey"
users = []
flowers = []
purchases = []

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

@app.get("/signup", response_class=HTMLResponse)
async def signup_form():
    return """
    <form action="/signup" method="post">
        Email: <input type="email" name="email"><br>
        Name: <input type="text" name="name"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Sign Up</button>
    </form>
    """

@app.post("/signup")
async def signup(email: str = Form(), name: str = Form(), password: str = Form()):
    for user in users:
        if user["email"] == email:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append({"email": email, "name": name, "password": password})
    return RedirectResponse("/login", status_code=303)

@app.get("/login", response_class=HTMLResponse)
async def login_form():
    return """
    <form action="/login" method="post">
        Email: <input type="email" name="email"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
    """

@app.post("/login")
async def login(email: str = Form(), password: str = Form()):
    user = next((u for u in users if u["email"] == email and u["password"] == password), None)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt(email)
    response = RedirectResponse("/profile", status_code=303)
    response.set_cookie(key="jwt", value=token, httponly=True)
    return response

@app.get("/profile", response_class=HTMLResponse)
async def profile(jwt_token: Optional[str] = Cookie(None)):
    if not jwt_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    email = decode_jwt(jwt_token)
    user = next((u for u in users if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return f"User Profile: {user['name']}, Email: {user['email']}"

@app.get("/flowers", response_class=HTMLResponse)
async def get_flowers():
    flower_list = "<ul>" + "".join(f"<li>{f['name']} - {f['price']} $ - <form action='/cart/items' method='post'><button name='flower_id' value='{f['id']}'>Add to Cart</button></form></li>" for f in flowers) + "</ul>"
    return f"""
    <form action="/flowers" method="post">
        Name: <input type="text" name="name"><br>
        Quantity: <input type="number" name="quantity"><br>
        Price: <input type="number" step="0.01" name="price"><br>
        <button type="submit">Add Flower</button>
    </form>
    {flower_list}
    """

@app.post("/flowers")
async def add_flower(name: str = Form(), quantity: int = Form(), price: float = Form()):
    flower_id = len(flowers) + 1
    flowers.append({"id": flower_id, "name": name, "quantity": quantity, "price": price})
    return RedirectResponse("/flowers", status_code=303)

@app.post("/cart/items")
async def add_to_cart(flower_id: int = Form(), cart: Optional[str] = Cookie(None)):
    cart_items = cart.split(',') if cart else []
    cart_items.append(str(flower_id))
    response = RedirectResponse("/flowers", status_code=303)
    response.set_cookie(key="cart", value=','.join(cart_items))
    return response

@app.get("/cart/items", response_class=HTMLResponse)
async def view_cart(cart: Optional[str] = Cookie(None)):
    if not cart:
        return "Your cart is empty"
    cart_items = cart.split(',')
    cart_flowers = [f for f in flowers if str(f["id"]) in cart_items]
    total_price = sum(f["price"] for f in cart_flowers)
    flower_list = "<ul>" + "".join(f"<li>{f['name']} - {f['price']} $</li>" for f in cart_flowers) + "</ul>"
    return f"{flower_list}<br>Total: {total_price} $"

@app.post("/purchased")
async def purchase(jwt_token: Optional[str] = Cookie(None), cart: Optional[str] = Cookie(None)):
    if not jwt_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    email = decode_jwt(jwt_token)
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")
    cart_items = cart.split(',')
    for flower_id in cart_items:
        purchases.append({"user_email": email, "flower_id": int(flower_id)})
    response = RedirectResponse("/purchased", status_code=303)
    response.delete_cookie(key="cart")
    return response

@app.get("/purchased", response_class=HTMLResponse)
async def view_purchases(jwt_token: Optional[str] = Cookie(None)):
    if not jwt_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    email = decode_jwt(jwt_token)
    user_purchases = [p for p in purchases if p["user_email"] == email]
    purchased_flowers = [f for f in flowers if any(p["flower_id"] == f["id"] for p in user_purchases)]
    flower_list = "<ul>" + "".join(f"<li>{f['name']} - {f['price']} $</li>" for f in purchased_flowers) + "</ul>"
    return f"Purchased Flowers: {flower_list}"
