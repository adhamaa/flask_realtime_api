import redis
from config import Config

# Connection pool for Redis client
pool = redis.ConnectionPool.from_url(Config.REDIS_URL, decode_responses=True, max_connections=100)
redis_client = redis.StrictRedis(connection_pool=pool)
