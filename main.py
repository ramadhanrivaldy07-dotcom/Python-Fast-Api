from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 250000}
]

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/products")
def get_products():
    return products