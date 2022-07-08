from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, crud
from app.api.deps import get_db, user_allow_crud


router = APIRouter()


# show all products
@router.get('/', response_model=List[schemas.Product])
async def read_products(
        db: AsyncSession = Depends(get_db),
        skip: int = 0,
        limit: int = 10,
        price_upto: Optional[int] = Query(
            default=None,
            gt=0,
            le=100_000
        ),
        price_from: Optional[int] = Query(
            default=None,
            gt=0,
            le=100_000
        ),
        order: str = Query(
            default='price_asc',
            enum=list(crud.ORDER.keys())
        ),
        provider: Optional[str] = Query(
            default=None,
            enum=['pr1', 'pr2']
        ),
):
    products = await crud.get_products(
        db,
        skip=skip,
        limit=limit,
        price_upto=price_upto,
        price_from=price_from,
        provider=provider,
        order=order
    )
    return products


@router.post('/', response_model=schemas.Product)
async def create_product(
        *,
        db: AsyncSession = Depends(get_db),
        product_in: schemas.ProductCreate,
        user_has_perm: bool = Depends(user_allow_crud)
):
    if user_has_perm:
        # check if product already exist
        product = await crud.get_product_by_name(db, product_in.name)
        if product:
            raise HTTPException(
                status_code=400,
                detail='Product with this name already exist'
            )
        product = await crud.create_product(db, product_in)
        return product
    else:
        raise HTTPException(status_code=403, detail='Not enough rights')
