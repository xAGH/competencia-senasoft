from flask import request, make_response, jsonify
from src.namespaces import RoomNamespace
from src.models import Model
from os import getenv, makedirs
import random

class RoomsService:

    def __init__(self) -> None:
        self.model: Model = Model()

    """
        :param characters_quantity — define la cantidad de carácteres que tendrá el enlace de una sala.
        :return — devuelve una cadena hexadecimal la cual corresponde al código de la sala.
    """
    def generate_room_code(self, characters_quantity: int=5):
        room_code: str = ""
        for i in range(characters_quantity):
            choice: str = random.choice("0123456789ABCDEF")
            room_code += choice
        return room_code
    
    def create_room(self):
        try:
            room = self.generate_room_code()
            RoomNamespace.rooms[room] = {
                "players": []
            } 
            response = make_response(jsonify({
                "room": room,
                "message": "The new room was created",
                "statusCode": 201
            }), 201)
            return response
        except Exception as e:
            return make_response(jsonify({
                "error": True,
                "message": "Exception: {}".format(e),
                "statusCode": 400
            }), 400)
