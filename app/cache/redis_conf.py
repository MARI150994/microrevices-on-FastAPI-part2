import redis

from app.core.config import settings

r = redis.from_url(settings.CACHE_HOST)