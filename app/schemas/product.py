from __future__ import annotations

from decimal import Decimal
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(max_length=30, min_length=3)
    article: str = Field(max_length=15, min_length=7)
    price: Decimal = Field(gt=0, lt=100_000, max_digits=6, decimal_places=2)
    available: int
    provider_id: int = Field(ge=1)

    class Config:
        schema_extra = {
            'example': {
                'name': 'apple',
                'article': '1234567',
                'price': 30.99,
                'available': 15,
                'provider_id': 1
            }
        }


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


