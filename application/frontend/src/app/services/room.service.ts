import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RoomService {
  constructor(private socket: Socket) {}

  joinRoom(roomCode: string): Observable<any> {
    const validCode = RoomService.isRoomCodeValid(roomCode);
    if (validCode) {
      this.socket.connect();
      return this.socket.fromEvent('connect').pipe((res) => {
        this.socket.emit('join', {
          'room' : roomCode
        });
        console.log('ROOM', res)
        return res
      });
    } else {
      return of(undefined);
    }
  }

  onRoomFull() : Observable<any> {
    return this.socket.fromEvent('room_full');
  }

  onJoinedRoom() : Observable<any> {
    return this.socket.fromEvent('user_joined');
  }

  onAlreadyOnRoom() : Observable<any> {
    return this.socket.fromEvent('user_is_on_room');
  }

  onRoomNotFound() : Observable<any> {
    return this.socket.fromEvent('room_not_found');
  }

  static isRoomCodeValid(roomCode: string | undefined): boolean {
    return roomCode != undefined && /[0-9A-F]{5}$/i.test(roomCode);
  }
}
