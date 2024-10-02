import json
from services.redis_client import redis_client
from services.socketio_service import socketio

# Redis subscriber for real-time updates
def redis_listener():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('data_updates')

    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            socketio.emit('data_update', data)

# # Function to start background threads
# def start_listener_threads():
#     listener_thread = threading.Thread(target=redis_listener)
#     listener_thread.daemon = True
#     listener_thread.start()

    # Add new threads here as needed in the future
    # Example:
    # new_thread = threading.Thread(target=your_new_function)
    # new_thread.daemon = True
    # new_thread.start()
