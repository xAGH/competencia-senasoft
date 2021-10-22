import { Injectable } from '@angular/core';
import { UserRoomIdentity } from '../interfaces/user-room-identity';

@Injectable({
  providedIn: 'root'
})
export class RoomSessionService {

  constructor() { }

  info? : UserRoomIdentity;
  userNumber?: number = -1;

  wipe() : void {
    this.info = undefined;
  }
}
