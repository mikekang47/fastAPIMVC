from pydantic import BaseModel, validator


class Product(BaseModel):
    name: str
    price: int


class ProductRequestData(Product):
    @validator('name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("product name must not be empty")
        return v

    @validator('price')
    def not_negative(cls, v):
        if v < 0:
            raise ValueError("product price must not be negative")
        return v


class ProductResponseData(Product):
    id: int

    class Config:
        orm_mode = True
