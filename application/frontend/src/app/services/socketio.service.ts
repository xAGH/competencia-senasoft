import { Injectable } from '@angular/core';
import { io } from 'socket.io-client';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SocketioService {

  socket = io(environment.websocket_endpoint);

  constructor() {
    this.socket.on('connect', () => {
      console.log('connected');
    });

    this.socket.on('disconnect', () => {
      console.log('disconnected from socket');
    });

    this.socket.on('connect_error', (err) => {
      console.error("Can't connect to socket endpoint", err);
    });

    this.socket.on('connect_failed', (err) => {
      console.error('Attemp to connect to socket unsuccessful', err);
    })
  }
}
