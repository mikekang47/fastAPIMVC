from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.application import product_application, prouduct
from app.core.session import get_db
from app.dto.product_request_data import ProductResponseData, ProductRequestData

router = APIRouter()


@router.post("/", response_model=ProductResponseData, status_code=status.HTTP_201_CREATED)
def create(*,
           db: Session = Depends(get_db),
           product_request: ProductRequestData):
    product = prouduct.create_product(db, product_request=product_request)
    return ProductResponseData(id=product.id, name=product.name, price=product.price)
