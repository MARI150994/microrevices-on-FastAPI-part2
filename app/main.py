import logging

import uvicorn
from fastapi import FastAPI

from app.models.db import database
from app.api.api import api_router
from app.cache import r

app = FastAPI()
app.include_router(api_router)


@app.on_event('startup')
async def startup():
    logging.info('db connect start')
    await database.connect()
    logging.info('db connect finish')
    logging.info('redis connect start')
    r.ping()
    logging.info('redis connect finish')


@app.on_event('shutdown')
async def shutdown():
    logging.info('db disconnect start')
    await database.disconnect()
    logging.info('db connect finish')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)