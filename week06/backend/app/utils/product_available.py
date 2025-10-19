from fastapi import HTTPException
from starlette import status
from backend.app.core.logger import logger



def product_available(value):
    if not value:
        logger.error("product not found to delete")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")