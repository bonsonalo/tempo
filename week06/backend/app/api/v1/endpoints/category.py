from fastapi import HTTPException, APIRouter
from starlette import status


from backend.app.model import models
from backend.app.model.category import Category, UpdateCategory
from backend.app.utils import authentication_check, product_available
from backend.app.core.config import user_dependency, db_dependency
from backend.app.utils.authentication_check import authentication_check




router = APIRouter(
    prefix= "category",
    tags= ["category"]
)


@router.post("/api/category", status_code=status.HTTP_201_CREATED, response_model=Category)
async def create_category(info: Category, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    # category= db.query(models.Categories).filter(models.Categories.name == info.name).first()
    # if not category:
    #     raise HTTPException(detail="category problem")
    db_add= models.Products(
        name= info.name,
        id= info.id
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

@router.get("/api/category", status_code=status.HTTP_200_OK)
async def get_category(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    results= db.query(models.Categories)
    return results

@router.get("/api/category/{id}", status_code=status.HTTP_200_OK)
async def get_product_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    category_by_id= db.query(models.Categories).filter(models.Categories.id == id).first()
    product_available(category_by_id)
    return category_by_id