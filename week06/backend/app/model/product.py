from pydantic import BaseModel, Field
from typing import Optional



class Products(BaseModel):
    name: str
    price: float
    SKU: str
    category_id: int
    supplier_id: int
    category_name: str
    supplier_name: str


class UpdateProduct(BaseModel):
    name: Optional[str]
    price: Optional[float]
    SKU: Optional[str]
    category_id: Optional[int]
    supplier_id: Optional[int]
    category_name: Optional[str]
