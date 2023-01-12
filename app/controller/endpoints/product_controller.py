from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app import application
from app.core.session import get_db
from app.dto.product_request_data import ProductResponseData, ProductRequestData

router = APIRouter()


@router.post("/", response_model=ProductResponseData, status_code=status.HTTP_201_CREATED)
def create(*,
           db: Session = Depends(get_db),
           product_request: ProductRequestData):
    product = application.product.create_product(db, product_request=product_request)
    return ProductResponseData(id=product.id, name=product.name, price=product.price)


@router.get("/", response_model=List[ProductResponseData])
def get_all(*, db: Session = Depends(get_db)):
    products = application.product.get_products(db)
    return [ProductResponseData(id=product.id, name=product.name, price=product.price) for product in products]


@router.put("/{id}", response_model=ProductResponseData)
def update(*,
           db: Session = Depends(get_db),
           id: int,
           product_request: ProductRequestData):
    product = application.product.update_product(db, id=id, product_request=product_request)
    return ProductResponseData(id=product.id, name=product.name, price=product.price)
