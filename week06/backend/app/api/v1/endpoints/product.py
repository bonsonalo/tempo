from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.model.product import Products, OrderBy, UpdateProduct
from backend.app.core.config import db_dependency, user_dependency, admin_dependency, superadmin_dependency
from starlette import status
from backend.app.model import models
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available 
from backend.app.core.logger import logger
from sqlalchemy import asc, desc



router= APIRouter(
    prefix= "/api/products",
    tags=["product"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(info: Products, db:db_dependency, current_user: admin_dependency):
    authentication_check(current_user)
    category_connect= db.query(models.Categories).filter(models.Categories.id == info.category_id).first()
    print("category_connect", category_connect)
    if not category_connect:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")
    
    

    supplier_connect= db.query(models.Suppliers).filter(models.Suppliers.id == info.supplier_id).first()
    if not supplier_connect:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier name not found")

    db_add= models.Products(
        name= info.name,
        price= info.price,
        SKU= info.SKU,
        category_id= category_connect.id,
        supplier_id= supplier_connect.id
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add



@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_products(current_user: user_dependency, db: db_dependency,
                       sort_by: str= Query("id"),
                       order: str= Query("asc"),
                       category_name: Optional[str] = Query(None), 
                       product_name: Optional[str] = Query(None)):
    authentication_check(current_user)

    query= db.query(models.Products)

    if category_name:
        category = db.query(models.Categories.name == category_name).first()
        if not category:
            logger.error(f"Category '{category_name}' not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{category_name} not found")
        query = query.filter(models.Products.category_id == category.id)

    if product_name:
        query= query.filter(models.Products.name == product_name)

    if not hasattr(models.Products, sort_by):
        logger.error(f"invalid sort field: {sort_by}")
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid sort field")
    column_to_sort= getattr(models.Products, sort_by)

    if order.lower() == "desc":
        query=query.order_by(column_to_sort.desc())
    elif order.lower() == "asc":
        query=query.order_by(column_to_sort.asc())
        

    results = query.all()

    if not results:
        logger.warning("No products found for given filters")
        raise HTTPException(status_code=404, detail="No products found")

    logger.info(f"Fetched {len(results)} products successfully")
    return results


@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def get_product_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_by_id= db.query(models.Products).filter(models.Products.id == id).first()
    product_available(product_by_id)
    return product_by_id

@router.put("/update/{id}")
async def update_product(id: int, updated_to: UpdateProduct, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Products).filter(models.Products.id == id).first()
    product_available(product_query)
    if updated_to.name is not None:
        product_query.name = updated_to.name
    if updated_to.price is not None:
        product_query.price = updated_to.price
    if updated_to.SKU is not None:
        product_query.SKU = updated_to.SKU

    db.commit()
    db.refresh(product_query)
    return product_query


@router.delete("/delete/{product_id}") 
async def delete_product(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    logger.info("starting")
    authentication_check(current_user)
    logger.info("seccessfully authenticated")
    product_query= db.query(models.Products).filter(models.Products.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    logger.info("deleted successfully")
    db.commit()
 
