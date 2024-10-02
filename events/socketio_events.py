import json
from services.redis_client import redis_client
from flask_socketio import SocketIO

def register_socketio_events(socketio: SocketIO):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')
        # Send the current data to the newly connected client
        current_data = json.loads(redis_client.get("realtime_data"))
        socketio.emit('data_update', current_data)

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')
