from typing import List

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

    def find_by_id(self, db: Session, *, id: int) -> Product:
        return db.query(Product) \
            .filter(Product.id == id) \
            .first()

    def find_all(self, db: Session, *, skip: int, limit: int) -> List[Product]:
        return db.query(Product) \
            .offset(skip) \
            .limit(limit) \
            .all()

    def delete_by_id(self, db: Session, *, id: int):
        db.query(Product).where(Product.id == id).delete()


product = ProductRepository()
