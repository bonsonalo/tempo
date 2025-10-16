from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.model.product import Products, SortBy, UpdateProduct
from backend.app.core.config import db_dependency, user_dependency
from starlette import status
from backend.app.model import models
from backend.app.utils.authentication_check import authentication_check
from backend.app.utils.product_available import product_available 



router= APIRouter(
    prefix= "/product",
    tags=["product"]
)


@router.post("/api/products", status_code=status.HTTP_201_CREATED)
async def create_product(info: Products, db:db_dependency, current_user:user_dependency):
    authentication_check(current_user)
    category_connect= db.query(models.Categories).filter(models.Categories.id == info.category_id).first()
    if not category_connect:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category problem")
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



@router.get("/api/products", status_code=status.HTTP_200_OK)
async def get_products(current_user: user_dependency, db: db_dependency,
                       sort_by: SortBy= Query(SortBy.asc),
                       category_name: Optional[str] = Query(None), 
                       product_name: Optional[str] = Query(None)):
    authentication_check(current_user)
    if product_name is not None and category_name is not None:
        get_category_full= db.query(models.Categories).filter(models.Categories.name == category_name).first()
        get_category_id= get_category_full.id
        get_products_by_category= db.query(models.Products).filter(models.Products.id == get_category_id).all()
        get_products_by_product_name= db.query(models.Products).filter(models.Products.name == product_name).all()
        both_search= [pro for pro in get_products_by_category if pro in get_products_by_product_name]
        if sort_by == "asc":
            return sorted(both_search, key=lambda p: p.name, reverse=False)
        elif sort_by == "desc":
            return sorted(both_search, reverse=True)
    
    elif product_name is not None:
        get_products_by_product_name= db.query(models.Products).filter(models.Products.name == product_name).all()
        return get_products_by_product_name
    elif category_name is not None:
        get_category_full= db.query(models.Categories).filter(models.Categories.name == category_name).first()
        get_category_id= get_category_full.id
        get_products_by_category= db.query(models.Products).filter(models.Products.category_id == get_category_id).all()
        if sort_by == "asc":
            return sorted(get_products_by_category, key=lambda p: p.name, reverse=False)
        elif sort_by == "desc":
            return sorted(get_products_by_category, key=lambda p: p.name, reverse=True)
    else:
        results= db.query(models.Products).all()
        if sort_by == "asc":
            return sorted(results, key=lambda p: p.name, reverse=False)
        elif sort_by == "desc":
            return sorted(results, key=lambda p: p.name, reverse=True)


@router.get("/api/products/{id}", status_code=status.HTTP_200_OK)
async def get_product_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_by_id= db.query(models.Products).filter(models.Products.id == id).first()
    product_available(product_by_id)
    return product_by_id

@router.put("/api/products/{id}")
async def update_product(id: int, updated_to: UpdateProduct, current_user: user_dependency, db: db_dependency):
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


@router.delete("/api/products/{id}") 
async def delete_product(product_id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Products).filter(models.Products.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.refresh(product_query)
    db.commit()
 
