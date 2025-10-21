from fastapi import APIRouter, HTTPException
from starlette import status 

from backend.app.model import models
from backend.app.model.stock import Stock, UpdateStock
from backend.app.core.config import user_dependency, db_dependency, user_authentication_dependency, admin_dependency, superadmin_dependency
from backend.app.service.stock_service import create_stock_service, get_stock_service, get_stock_by_key, update_stock_service, delete_stock_service
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available


router = APIRouter(
    prefix= "/api/stock",
    tags= ["stock"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_stock(info: Stock, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    try:
        return create_stock_service(info, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_stock(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    return get_stock_service(db)

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def get_stock_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    return get_stock_by_key(id, db)

@router.put("/update/{id}")
async def update_stock(id: int, updated_to: UpdateStock, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return update_stock_service(id, updated_to, db)


@router.delete("/delete/{id}") 
async def delete_stock(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    authentication_check(current_user)
    return delete_stock_service(product_id, db)