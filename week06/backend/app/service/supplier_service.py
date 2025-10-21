from backend.app.model import models
from starlette import status
from backend.app.model.supplier import Supplier, UpdateSupplier
from backend.app.utils.product_available import product_available
from sqlalchemy.orm import Session

# create
def create_supplier_service(info: Supplier, db: Session):
    db_add= models.Suppliers(
        name= info.name
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

#get_all

def get_supplier_service(db: Session):
    results= db.query(models.Suppliers).all()
    return results

#get by id

def get_supplier_by_key_service(id: int, db: Session):
    category_by_id= db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    product_available(category_by_id)
    return category_by_id

#update

def update_supplier_service(id: int, updated_to: UpdateSupplier, db: Session):
    product_query= db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    product_available(product_query)
    if updated_to.name is not None:
        product_query.name = updated_to.name

    db.commit()
    db.refresh(product_query)
    return product_query

#delete

def delete_supplier_service(product_id: int, db: Session):
    product_query= db.query(models.Suppliers).filter(models.Suppliers.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.refresh(product_query)
    db.commit()