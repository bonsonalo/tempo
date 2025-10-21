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