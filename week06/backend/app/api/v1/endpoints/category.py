from fastapi import APIRouter
from starlette import status


from backend.app.model import models
from backend.app.model.category import Category, UpdateCategory
from backend.app.utils.product_available import product_available
from backend.app.core.config import user_dependency, db_dependency
from backend.app.utils.authentication_check import authentication_check




router = APIRouter(
    prefix= "/category",
    tags= ["category"]
)


@router.post("/api/category", status_code=status.HTTP_201_CREATED, response_model=Category)
async def create_category(info: Category, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    db_add= models.Categories(
        name= info.name
        
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

@router.get("/api/category", status_code=status.HTTP_200_OK)
async def get_category(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    results= db.query(models.Categories).all()
    return results

@router.get("/api/category/{id}", status_code=status.HTTP_200_OK)
async def get_category_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    category_by_id= db.query(models.Categories).filter(models.Categories.id == id).first()
    product_available(category_by_id)
    return category_by_id

@router.put("/api/category/{id}")
async def update_category(id: int, updated_to: UpdateCategory, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Categories).filter(models.Categories.id == id).first()
    product_available(product_query)
    if updated_to.name is not None:
        product_query.name = updated_to.name

    db.commit()
    db.refresh(product_query)
    return product_query


@router.delete("/api/category/{id}") 
async def delete_category(product_id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    product_query= db.query(models.Categories).filter(models.Categories.id == product_id).first()
    product_available(product_query)
    db.delete(product_query)
    db.refresh(product_query)
    db.commit()
 
