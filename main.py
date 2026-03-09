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

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in Products:
        if product.id == product_id:
            return product
        
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    Products.append(product)
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index in range(len(Products)):
        if Products[index].id == product_id:
            Products[index] = updated_product
            return "Product updated successfully"
        
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index in range(len(Products)):
        if Products[index].id == product_id:
            del Products[index]
            return "Product deleted successfully"
        
    return {"error": "Product not found"}