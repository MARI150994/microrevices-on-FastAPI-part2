from __future__ import annotations

from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr


class ProviderBase(BaseModel):
    name: str = Field(min_length=5, max_length=30)
    email: EmailStr
    phone: str

    class Config:
        schema_extra = {
            'example': {
                'name': 'Very cool company',
                'email': 'coll.email@cool.com',
                'phone': '+77756399',
            }
        }


class ProviderCreate(ProviderBase):
    pass


class Provider(ProviderBase):
    id: int

    class Config:
        orm_mode = True
