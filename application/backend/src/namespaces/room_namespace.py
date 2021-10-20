from flask import request
from flask_socketio import rooms, send, emit, ConnectionRefusedError, join_room, leave_room
from flask_socketio.namespace import Namespace
from os import getenv

class RoomNamespace(Namespace):

    rooms: dict = {}
    users_in_room: list = []

    def on_connect(self):
        print("Connected", request.sid)
    
    def on_disconnect(self):
        print("Disconnected", request.sid)   
    
    def on_join(self, data):
        room = data['room']
        room_players = self.rooms["players"]
        username = f"player_{len(room_players)+1}"
        try:
            if len(room_players) >= int(getenv('ROOMS_LIMIT')):
                self.emit("room_full", {
                    "message": "Room is full"
                })
                return
            if username in room_players:
                self.emit("user_is_on_room", {
                    "messsage": f"El usuario {username} ya se encuentra en sala"
                })
                return
            self.enter_room(request.sid, room=room)
            new_player = {
                "name":username,
                "sid":request.sid,
                "cards": [],
                "cards_discovered": []
            }
            room_players.append(new_player)
            self.emit("user_joined", {
                "message": "User was joined",
                "users": room_players,
                "you" : new_player
            }, room=room)
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
            }, room=room)
        except ConnectionRefusedError:
            raise ConnectionRefusedError
        except Exception:
            raise Exception