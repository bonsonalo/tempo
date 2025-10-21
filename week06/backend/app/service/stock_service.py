from backend.app.model.stock import Stock, UpdateStock
from starlette import status
from sqlalchemy.orm import Session
from backend.app.model import models
from backend.app.utils.product_available import product_available


#create stock
def create_stock_service(info: Stock, db: Session):

    product_connect= db.query(models.Products).filter(models.Products.id == info.product_id).first()
    if not product_connect:
        raise ValueError("product name not found")
    supplier_connect= db.query(models.Suppliers).filter(models.Suppliers.id  == info.supplier_id).first()
    if not supplier_connect:
        raise ValueError("supplier name not found")
    db_add= models.Stock(
        quantity= info.quantity,
        movement_type= info.movement_type,
        date= info.date,
        supplier_id= supplier_connect.id,
        product_id= product_connect.id

    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

#get all stocks

def get_stock_service(db: Session):
    results= db.query(models.Stock).all()
    return results

#get by id

def get_stock_by_key(id: int, db: Session):
    category_by_id= db.query(models.Stock).filter(models.Stock.id == id).first()
    product_available(category_by_id)
    return category_by_id

#update


def update_stock_service(id: int, updated_to: UpdateStock, db: Session):
    product_query= db.query(models.Stock).filter(models.Stock.id == id).first()
    product_available(product_query)
    if updated_to.product_id is not None:
        product_query.product_id = updated_to.product_id
    if updated_to.quantity is not None:
        product_query.quantity= updated_to.quantity
    if updated_to.movement_type is not None:
        product_query.movement_type= updated_to.movement_type
    if updated_to.date is not None:
        product_query.date= updated_to.date
    if updated_to.supplier_id is not None:
        product_query.supplier_id= updated_to.supplier_id
    db.commit()
    db.refresh(product_query)
    return product_query

#delete

def delete_stock_service(product_id: int, db: Session):
    product_query= db.query(models.Stock).filter(models.Stock.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.commit()