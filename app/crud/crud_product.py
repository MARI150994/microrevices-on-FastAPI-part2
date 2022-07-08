from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models, schemas


# type of ordering and equal additional query for it
ORDER = {
    'price_asc': models.Product.price,
    'price_desc': models.Product.price.desc(),
    'name_asc': models.Product.name,
    'name_desc': models.Product.price.desc()
}


async def get_products(
        db: AsyncSession,
        skip: int,
        limit: int,
        price_upto: Optional[int],
        price_from: Optional[int],
        provider: Optional[str],
        order: str
) -> List[models.Product]:
    query = select(models.Product).offset(skip).limit(limit)
    if price_from:
        query = query.filter(models.Product.price >= price_from)
    if price_upto:
        query = query.filter(models.Product.price <= price_upto)
    if provider:
        query = query.join(models.Product.provider).filter(models.Provider.name == provider)
    query = query.order_by(ORDER.get(order))
    q = await db.execute(query)
    return q.scalars().all()


async def create_product(
        db: AsyncSession,
        product_in: schemas.ProductCreate
) -> models.Product:
    db_product = models.Product(
        name=product_in.name,
        article=product_in.article,
        provider_id=product_in.provider_id,
        price=product_in.price,
        available=product_in.available,
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_product_by_name(
        db: AsyncSession,
        name: str
) -> models.Product:
    query = select(models.Product).filter(models.Product.name == name)
    q = await db.execute(query)
    return q.scalars().first()
