
from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Depends, HTTPException, Query
from starlette import status

from backend.app.model import models
from backend.app.core.logger import logger
from backend.app.model.product import Products, UpdateProduct
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available 




def create_product_service(info: Products, db: Session):
    category_connect= db.query(models.Categories).filter(models.Categories.id == info.category_id).first()
    logger.info(f"category_connect {category_connect}")
    if not category_connect:
        raise ValueError("category not found")
    
    supplier_connect= db.query(models.Suppliers).filter(models.Suppliers.id == info.supplier_id).first()
    if not supplier_connect:
        raise ValueError("Supplier not found")  
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







def get_products_service(db: Session,
                    sort_by: str,
                    order: str,
                    category_name: Optional[str], 
                    product_name: Optional[str]):
    
    query= db.query(models.Products)

    if category_name:
        category = db.query(models.Categories.name == category_name).first()
        if not category:
            logger.error(f"Category '{category_name}' not found")
            raise ValueError(f"{category_name} not found")
        query = query.filter(models.Products.category_id == category.id)

    if product_name:
        query= query.filter(models.Products.name == product_name)

    if not hasattr(models.Products, sort_by):
        logger.error(f"invalid sort field: {sort_by}")
        raise  AttributeError(f"invalid sort field: {sort_by}")
    column_to_sort= getattr(models.Products, sort_by)

    if order.lower() == "desc":
        query=query.order_by(column_to_sort.desc())
    elif order.lower() == "asc":
        query=query.order_by(column_to_sort.asc())
        

    results = query.all()

    if not results:
        logger.warning("No products found for given filters")
        raise LookupError("No products found")

    logger.info(f"Fetched {len(results)} products successfully")
    return results



def update_product_service(id: int, updated_to: UpdateProduct, db: Session):
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

def delete_product_schema(product_id: int, db: Session):
    product_query= db.query(models.Products).filter(models.Products.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    logger.info("deleted successfully")
    db.commit()