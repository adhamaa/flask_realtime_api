import os
from flask_socketio import SocketIO
from config import DevelopmentConfig, ProductionConfig


# Determine the environment and set the config
environment = os.getenv('FLASK_ENV', 'development')
if environment == 'production':
    app_config = ProductionConfig
else:
    app_config = DevelopmentConfig

socketio = SocketIO(cors_allowed_origins="*", message_queue=app_config.REDIS_URL, async_mode=app_config.ASYNC_MODE)
