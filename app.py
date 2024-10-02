import eventlet
eventlet.monkey_patch()

import os
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from routes.api_routes import api_routes
from services.socketio_service import socketio
from services.thread_service import redis_listener
from events.socketio_events import register_socketio_events

# Determine the environment and set the config
environment = os.getenv('FLASK_ENV', 'development')
if environment == 'production':
    app_config = ProductionConfig
else:
    app_config = DevelopmentConfig

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(app_config)

# Attach the app to the SocketIO instance
socketio.init_app(app, 
                  message_queue=app_config.REDIS_URL, 
                  cors_allowed_origins="*", 
                  async_mode=app_config.ASYNC_MODE)

# Register Blueprints
app.register_blueprint(api_routes)

# Register SocketIO events
register_socketio_events(socketio)

if __name__ == '__main__':
    # Start Redis listener green thread with eventlet
    eventlet.spawn(redis_listener)
    # Use the Eventlet WSGI server in development
    socketio.run(app, debug=app_config.DEBUG, host=app_config.HOST, port=app_config.PORT)
