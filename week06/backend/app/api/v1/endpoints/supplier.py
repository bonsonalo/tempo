from starlette import status
from fastapi import APIRouter


from backend.app.utils.authentication_check import authentication_check
from backend.app.core.config import user_dependency, db_dependency
from backend.app.model import models
from backend.app.model.models import Suppliers
from backend.app.model.supplier import Supplier, UpdateSupplier
from backend.app.utils.product_available import product_available






router = APIRouter(
    prefix= "/supplier",
    tags= ["supplier"]
)


@router.post("/api/suppliers", status_code=status.HTTP_201_CREATED)
async def create_supplier(info: Supplier, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    db_add= models.Suppliers(
        name= info.name
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

@router.get("/api/suppliers", status_code=status.HTTP_200_OK)
async def get_supplier(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    results= db.query(models.Suppliers).all()
    return results

@router.get("/api/suppliers/{id}", status_code=status.HTTP_200_OK)
async def get_supplier_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    category_by_id= db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    product_available(category_by_id)
    return category_by_id

@router.put("/api/suppliers/{id}")
async def update_supplier(id: int, updated_to: UpdateSupplier, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    product_available(product_query)
    if updated_to.name is not None:
        product_query.name = updated_to.name

    db.commit()
    db.refresh(product_query)
    return product_query


@router.delete("/api/suppliers/{id}") 
async def delete_supplier(product_id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Suppliers).filter(models.Suppliers.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.refresh(product_query)
    db.commit()