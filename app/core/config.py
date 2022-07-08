from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    SECRET_KEY: str = 'O6Pm30ZfK5i-Z8fE7Q699thw'
    API_URL_PREFIX: str = '/api/v1'
    SQLALCHEMY_PG_CONN_URI: str = 'postgresql+asyncpg://user:password@localhost:5431/stock'
    CACHE_HOST: str = 'redis://localhost:6379'
    LOGIN_APP_URL: str = 'http://0.0.0.0:8000/login/perm'


settings = Settings()
