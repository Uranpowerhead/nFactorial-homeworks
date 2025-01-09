from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello,nFactorial!"}

@app.post("/meaning-of-life")
def post_meaning_of_life():
    return {"meaning": 42}

@app.get("/{num}")
def factorial(num: int):
    if num < 0:
        return {'Error': 'num must be positive'}
    if num == 0:
        return {1}
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return {result}

