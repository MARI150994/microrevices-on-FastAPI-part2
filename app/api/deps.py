from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
import aiohttp


from app.models.db import async_session
from app.core.config import settings
from app import models, schemas, crud
from app.cache import r

oauth_scheme = OAuth2PasswordBearer(
    tokenUrl=f'/login/token'
)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def user_allow_crud(access_token: str = Header()):
    # check cache wih access token, if in cache and return True then allow
    user_is_admin = r.get(access_token)

    if user_is_admin is None:
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {access_token}'}

        # TODO RabbitMQ
        async def check_perm():
            async with aiohttp.ClientSession() as session:
                async with session.post(url=settings.LOGIN_APP_URL,
                                        headers=headers) as r:
                    if r.status == 403:
                        raise HTTPException(status_code=403,
                                            detail='Invalid token')
                    print('RESULT FROM check_perm', r)
                    return await r.json()

        user_is_admin = await check_perm()

    if int(user_is_admin):
        return True
    if not int(user_is_admin):
        raise HTTPException(status_code=403, detail='Not enough rights')
    return access_token

