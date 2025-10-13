from pydantic import BaseModel



class Supplier(BaseModel):
    id: int
    name: str

class UpdateSupplier(Supplier):
    pass