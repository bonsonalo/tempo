from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional



class Products(BaseModel):
    name: str
    price: float
    SKU: str
    category_id: int
    supplier_id: int


class UpdateProduct(BaseModel):
    name: Optional[str]= Field(None)
    price: Optional[float]= Field(None)
    SKU: Optional[str]= Field(None)
    category_id: Optional[int]= Field(None)
    supplier_id: Optional[int]= Field(None)
