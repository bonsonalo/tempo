from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class Stock(BaseModel):
    product_id: int
    quantity: int
    movement_type: str
    date: date
    supplier_id: int
    product_name: str
    supplier_name: str


class UpdateStock(Stock):
    product_id: Optional[int]
    quantity: Optional[int]
    movement_type: Optional[str]
    date: Optional[date]
    supplier_id: Optional[int]