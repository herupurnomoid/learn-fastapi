from fastapi import FastAPI
from models import Product

app = FastAPI()

Products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=499.99, quantity=20),
    Product(id=3, name="Tablet", description="10-inch touchscreen tablet", price=299.99, quantity=15),
    Product(id=4, name="Headphones", description="Wireless noise-cancelling headphones", price=149.99, quantity=30),
]

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

@app.get("/products")
def get_all_products():
    return Products
