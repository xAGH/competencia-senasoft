from flask_socketio import send, emit, ConnectionRefusedError, join_room, leave_room
from flask_socketio.namespace import Namespace

class RoomNamespace(Namespace):
    
    async def on_connection(self, sid):
        print("Connected", sid)
    
    async def on_disconnect(self, sid):
        print("Disconnected", sid)
    
    async def on_join(self, sid, data):
        username = data['username']
        room = data['room']
        await self.enter_room(sid, room)
        await self.send({
            "username": username,
            "message": "has entered the room"
        }, to=room)
    
    async def on_leave(self, sid, data):
        pass