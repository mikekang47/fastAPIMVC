from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.session import get_db
from app.domain.product import Product


class ProductRepository:
    def save(self, db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product


product = ProductRepository()
