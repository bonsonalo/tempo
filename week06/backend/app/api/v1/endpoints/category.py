from fastapi import APIRouter, Query, HTTPException
from starlette import status


from backend.app.model import models
from backend.app.model.category import Category, UpdateCategory
from backend.app.service.category_service import create_category_service, get_category_schema, get_category_by_id_service, update_category_service, delete_category_service
from backend.app.utils.product_available import product_available
from backend.app.core.config import user_dependency, db_dependency, user_authentication_dependency, admin_dependency, superadmin_dependency
from backend.app.utils.authentication_check import authentication_check
from backend.app.core.logger import logger



router = APIRouter(
    prefix= "/api/category",
    tags= ["category"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Category)
async def create_category(info: Category, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return create_category_service(info, db)

@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_category(current_user: user_dependency, db: db_dependency, 
                       sort_by: str= Query("id"),
                       order: str= Query("asc")):
    authentication_check(current_user)
    return get_category_schema(db, sort_by, order)
    

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def get_category_by_id(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    logger.info("successfully authenticated")
    try:
        return get_category_by_id_service(id, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= str(e))

@router.put("/update/{id}")
async def update_category(id: int, updated_to: UpdateCategory, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return update_category_service(id, updated_to, db)


@router.delete("/delete/{product_id}") 
async def delete_category(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    authentication_check(current_user)
    logger.info("successfully authorized")
    return delete_category_service(product_id, db)
 
