import { Component, ElementRef, OnInit, setTestabilityGetter, ViewChild } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observer } from 'rxjs';
import { filter } from 'rxjs/operators';
import { RoomService } from 'src/app/services/room.service';

@Component({
  selector: 'app-hall',
  templateUrl: './hall.component.html',
  styleUrls: ['./hall.component.scss'],
  host: { class: 'full-extent' },
})
export class HallComponent implements OnInit {
  @ViewChild('roomInput') roomInput?: ElementRef;

  constructor(private socket: Socket, private roomSrv: RoomService) {}

  ngOnInit(): void {
    const testObserver : Observer<any> = {
      next: (res:any) => console.log(res),
      error: (err: any) => console.error(err),
      complete: () => console.log('Complete')
    };

    this.roomSrv.onJoinedRoom().subscribe(testObserver);
    this.roomSrv.onAlreadyOnRoom().subscribe(testObserver);
    this.roomSrv.onRoomFull().subscribe(testObserver);
    this.roomSrv.onRoomNotFound().subscribe(testObserver);
  }

  validCode = false;

  private getRoomCode(): string | undefined {
    return this.roomInput?.nativeElement.value ?? undefined;
  }

  onJoinRoom() {
    const roomCode: string | undefined = this.getRoomCode();
    console.log('Joining with code:', roomCode);
    // Valido el código hexadecimal
    if (roomCode != undefined) this.roomSrv.joinRoom(roomCode);

  }

  onCreateRoom() {
    console.log('Creating');
  }
}
