from backend.app.model.stock import Stock, UpdateStock
from starlette import status
from sqlalchemy.orm import Session
from backend.app.model import models


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

#get stocks by id

