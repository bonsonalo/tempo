from starlette import status
from fastapi import APIRouter


from backend.app.service.supplier_service import create_supplier_service, get_supplier_service, get_supplier_by_key_service, update_supplier_service, delete_supplier_service
from backend.app.utils.authentication_check import authentication_check
from backend.app.core.config import user_dependency, db_dependency, user_authentication_dependency, admin_dependency, superadmin_dependency
from backend.app.model import models
from backend.app.model.models import Suppliers
from backend.app.model.supplier import Supplier, UpdateSupplier
from backend.app.utils.product_available import product_available






router = APIRouter(
    prefix= "/api/supplier",
    tags= ["supplier"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_supplier(info: Supplier, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return create_supplier_service(info, db)

@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_supplier(current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    return get_supplier_service(db)

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def get_supplier_by_key(id: int, current_user: user_dependency, db: db_dependency):
    authentication_check(current_user)
    return get_supplier_by_key_service(id, db)

@router.put("/update/{id}")
async def update_supplier(id: int, updated_to: UpdateSupplier, current_user: admin_dependency, db: db_dependency):
    authentication_check(current_user)
    return update_supplier_service(id, updated_to, db)


@router.delete("/delete/{product_id}") 
async def delete_supplier(product_id: int, current_user: superadmin_dependency, db: db_dependency):
    authentication_check(current_user)
    return delete_supplier_service(product_id, db)