import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable, of } from 'rxjs';
import { filter, tap } from 'rxjs/operators';
import { PlayerInfo } from '../interfaces/player-info';
import { UserRoomIdentity } from '../interfaces/user-room-identity';

@Injectable({
  providedIn: 'root',
})
export class RoomService {
  constructor(private socket: Socket, private http: HttpClient) {}

  currentRoomCode?: string;

  joinRoom(roomCode: string): Observable<any> {
    const validCode = RoomService.isRoomCodeValid(roomCode);
    if (validCode) {
      this.socket.connect();
      return this.socket.fromEvent('connect').pipe((res) => {
        this.currentRoomCode = roomCode;
        this.socket.emit('join', {
          room: roomCode,
        });
        return res;
      });
    } else {
      return of(undefined);
    }
  }

  onRoomFull(): Observable<any> {
    return this.socket.fromEvent('room_full');
  }

  onJoinedRoom(): Observable<UserRoomIdentity> {
    return this.socket.fromEvent('user_joined');
  }

  onLeftRoom(): Observable<any> {
    return this.socket.fromEvent('user_leave');
  }

  onAlreadyOnRoom(): Observable<any> {
    return this.socket.fromEvent('user_is_on_room');
  }

  onRoomNotFound(): Observable<any> {
    return this.socket.fromEvent('room_not_found');
  }

  startGame(roomCode: string) {
    this.socket.emit('game_start', { room: roomCode });
  }

  onGameStart(): Observable<any> {
    return this.socket.fromEvent('game_start');
  }

  onUserDisconnect(): Observable<any> {
    return this.socket.fromEvent('disconnect').pipe(
      tap(
        this.socket.emit('request_disconnection', {
          room: this.currentRoomCode,
        })
      )
    );
  }

  onMessage() {
    return this.socket.fromEvent('message');
  }

  sendMessage(data: {message: string, player: any, room: string}) {
    this.socket.ioSocket.send(data);
  }

  requestRoomInfo(data: any) {
    this.socket.emit('request_room_info', data);
  }

  onGetRoomInfo() : Observable<any>{
    return this.socket.fromEvent('get_room_info');
  }

  checkRoomExists(roomCode: string): Observable<any> {
    return this.http
      .get('room?code=' + roomCode)
      .pipe(filter((res: any) => res != null && !!res && 'exists' in res));
  }

  leaveRoom(user: PlayerInfo) {
    this.socket.emit('leave', {
      room: this.currentRoomCode,
      username: user.name,
    });
  }

  createAndJoinRoom() {
    this.http.post('create_room', {}).subscribe((res : any) => {
      const roomCode = res.room;
      this.joinRoom(roomCode);
    });
  }

  getSocketID() {
    return this.socket.ioSocket.id;
  }

  static isRoomCodeValid(roomCode: string | undefined): boolean {
    return roomCode != undefined && /[0-9A-F]{5}$/i.test(roomCode);
  }
}
