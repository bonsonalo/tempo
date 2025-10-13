from fastapi import HTTPException
from starlette import status



def product_available(value):
    if not value:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")