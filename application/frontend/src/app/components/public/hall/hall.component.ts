import {
  Component,
  ElementRef,
  OnInit,
  OnDestroy,
  setTestabilityGetter,
  ViewChild,
} from '@angular/core';
import { Router } from '@angular/router';
import { Socket } from 'ngx-socket-io';
import { Observer, Subscription } from 'rxjs';
import { filter, tap } from 'rxjs/operators';
import { UserRoomIdentity } from 'src/app/interfaces/user-room-identity';
import { RoomSessionService } from 'src/app/services/room-session.service';
import { RoomService } from 'src/app/services/room.service';

@Component({
  selector: 'app-hall',
  templateUrl: './hall.component.html',
  styleUrls: ['./hall.component.scss'],
  host: { class: 'full-extent' },
})
export class HallComponent implements OnInit, OnDestroy {
  @ViewChild('roomInput') roomInput?: ElementRef;

  constructor(
    private socket: Socket,
    private roomSrv: RoomService,
    private roomSessionSrv: RoomSessionService,
    private router: Router
  ) {}

  subscriptions: Subscription[] = [];

  ngOnInit(): void {
    const testObserver: Observer<any> = {
      next: (res: any) => console.log(res),
      error: (err: any) => console.error(err),
      complete: () => console.log('Complete'),
    };

    this.subscriptions.push(
      this.roomSrv
        .onJoinedRoom()
        .pipe(
          tap((res: UserRoomIdentity) => {
            // Logica de inicio
            this.roomSessionSrv.info = res;
            this.router.navigate([
              'lobby',
              { code: this.roomSrv.currentRoomCode },
            ]);
          })
        )
        .subscribe(testObserver)
    );
    this.subscriptions.push(
      this.roomSrv.onAlreadyOnRoom().subscribe(testObserver)
    );
    this.subscriptions.push(this.roomSrv.onRoomFull().subscribe(testObserver));
    this.subscriptions.push(
      this.roomSrv.onRoomNotFound().subscribe(testObserver)
    );
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach((sub) => sub.unsubscribe());
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
