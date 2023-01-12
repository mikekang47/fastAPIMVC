from fastapi import APIRouter

from app.controller.endpoints.product_controller import router

api_router = APIRouter()
api_router.include_router(router, prefix="/products", tags=["products"])