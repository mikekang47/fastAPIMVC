from typing import List

from sqlalchemy.orm import Session

from app.domain.product import Product
from app.dto.product_request_data import ProductRequestData
from app.infra import product_repository


class ProductApplication:
    def create_product(self, db: Session, *, product_request: ProductRequestData) -> Product:
        product = Product(name=product_request.name, price=product_request.price)
        return product_repository.product.save(db, product)

    def get_product(self, db: Session, *, id: int) -> Product:
        return product_repository.product.find_by_id(db, id=id)

    def get_products(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Product]:
        return product_repository.product.find_All(db, skip=skip, limit=limit)

    def update_product(self, db: Session, *, id: int, product_request: ProductRequestData) -> Product:
        product = product_repository.product.find_by_id(db, id=id)
        product.update_product(product_request.name, product_request.price)
        return product_repository.product.save(db, product)


product = ProductApplication()
