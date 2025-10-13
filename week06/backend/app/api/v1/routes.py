from fastapi import APIRouter




from backend.app.api.v1.endpoints.auth import router as auth_router
from backend.app.api.v1.endpoints.category import router as category_router
from backend.app.api.v1.endpoints.product import router as product_router
from backend.app.api.v1.endpoints.stock import router as stock_router
from backend.app.api.v1.endpoints.supplier import router as supplier_router


routers = APIRouter()
router_list = [auth_router, category_router, product_router, stock_router, supplier_router]

for router in router_list:
    routers.include_router(router)