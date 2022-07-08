from typing import Any, List, Optional

from fastapi import APIRouter, Query, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, crud, models
from app.api.deps import get_db, user_allow_crud

router = APIRouter()


# show all products
@router.get('/', response_model=List[schemas.Provider])
async def read_providers(
        db: AsyncSession = Depends(get_db),
        skip: int = 0,
        limit: int = 10):
    providers = await crud.get_providers(
        db,
        skip=skip,
        limit=limit,
    )
    return providers


@router.post('/', response_model=schemas.Provider)
async def create_provider(
        *,
        db: AsyncSession = Depends(get_db),
        provider_in: schemas.ProviderCreate,
        user_has_perm: bool = Depends(user_allow_crud)
):
    if user_has_perm:
        provider = await crud.get_providerby_name(db, provider_in.name)
        if provider:
            raise HTTPException(
                status_code=400,
                detail='Product with this name already exist'
            )
        provider = await crud.create_provider(db, provider_in)
        return provider
    raise HTTPException(status_code=403, detail='Not enough rights')

