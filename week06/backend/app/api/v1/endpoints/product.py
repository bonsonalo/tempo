from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.model.product import Products, UpdateProduct
from backend.app.core.config import db_dependency, user_dependency, admin_dependency, superadmin_dependency
from starlette import status
from backend.app.model import models
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available 
from backend.app.core.logger import logger
from sqlalchemy import asc, desc
from backend.app.service.product_service import get_products_service, create_product_service, update_product_service, delete_product_schema



router= APIRouter(
    prefix= "/api/products",
    tags=["product"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(info: Products, db:db_dependency, current_user: admin_dependency):
    authentication_check(current_user)
    try:
        return create_product_service(info, db)
    except ValueError as e:
        logger.error(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= str(e))




@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_products(current_user: user_dependency, db: db_dependency,
                       sort_by: str= Query("id"),
                       order: str= Query("asc"),
                       category_name: Optional[str] = Query(None), 
                       product_name: Optional[str] = Query(None)):
    
    authentication_check(current_user)
    try:
        return get_products_service(db, sort_by, order, category_name, 
                        product_name)
    except ValueError as e:
        logger.error(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= str(e))
    except AttributeError as e:
        logger.error(str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= str(e))
    except LookupError:
        logger.warning(str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception:
        logger.error("Unexpected error")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    


@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def get_product_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_by_id= db.query(models.Products).filter(models.Products.id == id).first()
    product_available(product_by_id)
    return product_by_id

@router.put("/update/{id}")
async def update_product(id: int, updated_to: UpdateProduct, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return update_product_service(id, updated_to, db)


@router.delete("/delete/{product_id}") 
async def delete_product(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    logger.info("starting")
    authentication_check(current_user)
    logger.info("seccessfully authenticated")
    return delete_product_schema(product_id, db)
 
