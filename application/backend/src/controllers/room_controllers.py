from flask import request, make_response, jsonify
from flask.views import MethodView
from src.services.rooms_service import RoomsService

class RoomController(MethodView):

    rooms: dict = {}

    def __init__(self) -> None:
        self.room_service: RoomsService = RoomsService()    
    
    def get(self):
        return "Room controller"

    def post(self):
        if request.is_json:
            owner = request.json['owner']
            room = self.room_service.generate_room_code()
            return ""
        response = make_response(jsonify({
            "message": "Bad request. Please send a Json format",
            "statusCode": 400
        }), 400)
        return response