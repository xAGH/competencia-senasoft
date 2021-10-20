from flask import request, make_response, jsonify
from flask.views import MethodView
from flask_socketio import send, emit, ConnectionRefusedError
from flask_socketio.namespace import Namespace
from src.services.rooms_service import RoomsService

class RoomNamespace(MethodView, Namespace):
    
    rooms: dict = {}

    def __init__(self) -> None:
        self.room_service: RoomsService = RoomsService()
    
    def post(self):
        if request.is_json:
            owner = request.json['owner']
            room = self.room_service.generate_room_code()
        response = make_response(jsonify({
            "message": "Bad request. Please send a Json format",
            "statusCode": 400
        }), 400)
        return response
    
    async def on_connection(self, sid):
        print("Connected", sid)
    
    async def on_disconnect(self, sid):
        print("Disconnected", sid)
    
    async def on_message(self, sid):
        pass