from pydantic import BaseModel



class Category(BaseModel):
    name: str


class UpdateCategory(Category):
    pass