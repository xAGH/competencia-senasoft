from flask import request
from flask_socketio import rooms, send, emit, ConnectionRefusedError, join_room, leave_room
from flask_socketio.namespace import Namespace
from os import getenv

class RoomNamespace(Namespace):

    rooms: dict = {}
    users_in_room: list = []

    def on_connect(self):
        print("Connected")
    
    def on_disconnect(self):
        print("Disconnected")
    
    def on_join(self, data):
        room = data['room']
        username = f"player_{len(self.users_in_room)+1}"
        try:
            if len(self.users_in_room) >= int(getenv('ROOMS_LIMIT')):
                self.emit("room_full", {
                    "message": "Room is full"
                }, room=room)
            self.enter_room(request.sid, room=room)
            self.users_in_room.append(username)
            self.emit("user_joined", {
                "message": "User was joined",
                "users": self.users_in_room
            })
        except ConnectionRefusedError as cr:
            raise ConnectionRefusedError
        except Exception as e:
            raise Exception

    def on_leave(self, data):
        room = data['room']
        username = data['username']
        try:
            self.users_in_room.index(username)
            self.users_in_room.remove(username)
            self.leave_room(request.sid, room)
            self.emit("user_leave", {
                "message": f"User {username} left",
                "users": self.users_in_room
            })
        except ConnectionRefusedError:
            raise ConnectionRefusedError
        except Exception:
            raise Exception