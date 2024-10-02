from flask import Blueprint, request, jsonify
import json
from services.redis_client import redis_client
from services.socketio_service import socketio

api_routes = Blueprint('api_routes', __name__)

data_key = "realtime_data"

# Initialize the in-memory data if not present in Redis
if not redis_client.exists(data_key):
    redis_client.set(data_key, json.dumps({"value": 0}))

# hello world
@api_routes.route('/', methods=['GET'])
def hello_world(): 
    return jsonify({ 'message' : 'hello world' }), 200

# Endpoint to update the data
@api_routes.route('/update', methods=['POST'])
def update_data():
    new_value = request.json.get('value')
    if new_value is not None:
        # Update the data in Redis
        updated_data = {"value": new_value}
        redis_client.set(data_key, json.dumps(updated_data))
        
        # Emit the updated data to all connected clients
        socketio.emit('data_update', updated_data)
        return jsonify({"message": "Data updated", "data": updated_data}), 200
    return jsonify({"error": "Invalid data"}), 400

# Endpoint to get the current data
@api_routes.route('/data', methods=['GET'])
def get_data():
    # Retrieve data from Redis
    current_data = json.loads(redis_client.get(data_key))
    return jsonify(current_data), 200
