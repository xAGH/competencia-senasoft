import { Component } from '@angular/core';
import { SocketioService } from './services/socketio.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'bugfinder';

  constructor(private socketSrv: SocketioService) {
    const data = { username: 'user', room: 'ABCDE' };
    socketSrv.socket.emit('join', socketSrv.socket.id, data);
    socketSrv.socket.on('message', (data) => {
      console.log(data);
    }
    );
  }

  joinRoom(room : string) {
    if (this.socketSrv.socket.connected) {
      const data = {'username' : 'USER', room};
      this.socketSrv.socket.emit('join', data);
    }
  }

  connectToSocket() {
    if (this.socketSrv.socket.disconnected) this.socketSrv.socket.connect();
  }

  disconnectFromSocket() {
    if (this.socketSrv.socket.connected) {
      this.socketSrv.socket.disconnect();
    }
  }
}
