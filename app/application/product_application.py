from sqlalchemy.orm import Session

from app.domain.product import Product
from app.dto.product_request_data import ProductRequestData
from app.infra import product_repository


class ProductApplication:
    def create_product(self, db: Session, *, product_request: ProductRequestData) -> Product:
        product = Product(name=product_request.name, price=product_request.price)
        return product_repository.product.save(db, product)


prouduct = ProductApplication()
