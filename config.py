import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret!")
    REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")
    HOST = '0.0.0.0'
    PORT = '5000'

class DevelopmentConfig(Config):
    DEBUG = True
    ASYNC_MODE = 'gevent'  # or 'threading' for local development

class ProductionConfig(Config):
    DEBUG = True
    ASYNC_MODE = 'eventlet'  # Use 'gevent' for uWSGI
