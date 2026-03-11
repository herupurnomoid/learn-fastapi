from fastapi import Depends, FastAPI
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

Products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=499.99, quantity=20),
    Product(id=3, name="Tablet", description="10-inch touchscreen tablet", price=299.99, quantity=15),
    Product(id=4, name="Headphones", description="Wireless noise-cancelling headphones", price=149.99, quantity=30),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count()
    
    if count == 0:
        for product in Products:
            db.add(database_models.Product(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                quantity=product.quantity
            ))
        db.commit()

init_db()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {
        "message": "Product created successfully",
        "product": db_product
    }

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    
    if db_product:
        db.query(database_models.Product).filter(database_models.Product.id == product_id).update({
            database_models.Product.name: updated_product.name,
            database_models.Product.description: updated_product.description,
            database_models.Product.price: updated_product.price,
            database_models.Product.quantity: updated_product.quantity
        })
        db.commit()
        updated = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
        return {
            "message": "Product updated successfully",
            "product": updated
        }
            
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
        
    return {"error": "Product not found"}