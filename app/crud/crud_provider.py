from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import models, schemas


async def get_providers(
        db: AsyncSession,
        skip: int,
        limit: int,
) -> models.Provider:
    query = select(models.Provider).offset(skip).limit(limit)
    q = await db.execute(query)
    return q.scalars().all()


async def create_providers(
        db: AsyncSession,
        provider_in: schemas.ProviderCreate
) -> models.Provider:
    db_provider = models.Provider(
        name=provider_in.name,
        email=provider_in.email,
        phone=provider_in.phone
    )
    db.add(db_provider)
    await db.commit()
    await db.refresh(db_provider)
    return db_provider


# TODO class for CRUD Product and Provider
async def get_provider_by_name(
        db: AsyncSession,
        name: str
) -> models.Provider:
    query = select(models.Provider).filter(models.Provider.name == name)
    q = await db.execute(query)
    return q.scalars().first()


