from flask import request
from flask_socketio import send, emit, ConnectionRefusedError, join_room, leave_room
from flask_socketio.namespace import Namespace

class RoomNamespace(Namespace):

    rooms: dict = {}

    def on_connect(self):
        print("Connected")
    
    def on_disconnect(self):
        print("Disconnected")
    
    def on_join(self, data):
        username = data['username']
        room = data['room']
        self.enter_room(request.sid, room)
        self.send({
            "username": username,
            "message": "has entered the room"
        }, room=room)
    
    def on_leave(self, data):
        pass