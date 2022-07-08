from fastapi import APIRouter

from app.api.endpoints import products, provider

api_router = APIRouter()
api_router.include_router(products.router, prefix='/products', tags=['products'])
api_router.include_router(provider.router, prefix='/providers', tags=['providers'])

