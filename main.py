from fastapi import Depends, FastAPI
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to Telusko API"}

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    """Get all products"""
    products = db.query(database_models.Product).all()
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """Get product by ID"""
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if product:
        return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    """Create a new product"""
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
    return db_product

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    """Update a product"""
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    
    if product:
        db.query(database_models.Product).filter(database_models.Product.id == product_id).update({
            database_models.Product.name: updated_product.name,
            database_models.Product.description: updated_product.description,
            database_models.Product.price: updated_product.price,
            database_models.Product.quantity: updated_product.quantity
        })
        db.commit()
        updated = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
        return updated
            
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product"""
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}
        
    return {"error": "Product not found"}