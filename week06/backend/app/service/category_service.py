from backend.app.model import models
from backend.app.model.category import Category, UpdateCategory
from backend.app.core.logger import logger



from sqlalchemy.orm import Session

from backend.app.utils.product_available import product_available








#create category
def create_category_service(info: Category, db: Session):
    db_add= models.Categories(
        name= info.name
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

#get ALL categories
def get_category_schema(db: Session, 
                       sort_by: str,
                       order: str):
    query= db.query(models.Categories)
    if not hasattr(models.Categories, sort_by):
        logger.error(f"invalid sort field: {sort_by}")
        raise AttributeError(f"invalid sort field: {sort_by}")
    column_to_sort= getattr(models.Categories, sort_by)

    if order.lower() == "desc":
        query= query.order_by(column_to_sort.desc())
    elif order.lower() == "asc":
        query= query.order_by(column_to_sort.asc())


    results= query.all()
    if not results:
        logger.warning("No product with the give filter")
        raise LookupError("No product found")
    logger.info(f"fetched {len(results)} products successfully")

    return results


#get by id

def get_category_by_id_service(id: int,db: Session):
    category_by_id= db.query(models.Categories).filter(models.Categories.id == id).first()
    
    if not category_by_id:
        raise ValueError(f"no category found with id: {id}")
    return category_by_id