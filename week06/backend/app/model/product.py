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
    name: Optional[str]
    price: Optional[float]
    SKU: Optional[str]
    category_id: Optional[int]
    supplier_id: Optional[int]
class SortBy(str, Enum):
    asc= "asc"
    desc= "desc"