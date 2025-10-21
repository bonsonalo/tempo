from fastapi import APIRouter, HTTPException
from starlette import status 

from backend.app.model import models
from backend.app.model.stock import Stock, UpdateStock
from backend.app.core.config import user_dependency, db_dependency, user_authentication_dependency, admin_dependency, superadmin_dependency
from backend.app.service.stock_service import create_stock_service
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available


router = APIRouter(
    prefix= "/stock",
    tags= ["stock"]
)


@router.post("/api/stock", status_code=status.HTTP_201_CREATED)
async def create_stock(info: Stock, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    try:
        return create_stock_service(info, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/api/stock", status_code=status.HTTP_200_OK)
async def get_stock(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    results= db.query(models.Stock).all()
    return results

@router.get("/api/stock/{id}", status_code=status.HTTP_200_OK)
async def get_stock_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    category_by_id= db.query(models.Stock).filter(models.Stock.id == id).first()
    product_available(category_by_id)
    return category_by_id

@router.put("/api/stock/{id}")
async def update_stock(id: int, updated_to: UpdateStock, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
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


@router.delete("/api/category/{id}") 
async def delete_stock(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Stock).filter(models.Stock.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.refresh(product_query)
    db.commit()