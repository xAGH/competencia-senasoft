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
import { ToastrService } from 'ngx-toastr';
import { Observer, Subscription } from 'rxjs';
import { filter, tap } from 'rxjs/operators';
import { UserRoomIdentity } from 'src/app/interfaces/user-room-identity';
import { RoomSessionService } from 'src/app/services/room-session.service';
import { RoomService } from 'src/app/services/room.service';
import { SpinnerService } from 'src/app/services/spinner.service';

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
    private router: Router,
    private toastr: ToastrService,
    private spinner: SpinnerService,
  ) {}

  subscriptions: Subscription[] = [];

  ngOnInit(): void {
    const testObserver: Observer<any> = {
      next: (res: any) => console.log(res),
      error: (err: any) => console.error(err),
      complete: () => console.log('Complete'),
    };

    this.roomSrv.onJoinedRoom().subscribe((res) => {
      // Logica de inicio
      if (res.you.sid == this.socket.ioSocket.id) {
        this.spinner.hideSpinner();
        this.roomSessionSrv.info = res;
        this.router.navigate(['lobby'], {
          queryParams: { code: this.roomSrv.currentRoomCode },
        });
      }
    });
    this.subscriptions.push(
      this.roomSrv.onAlreadyOnRoom().subscribe((res) => {
        this.spinner.hideSpinner();
        this.toastr.success('Ya estás dentro de esta sala');
      })
    );
    this.subscriptions.push(
      this.roomSrv.onRoomFull().subscribe((_) => {
        this.spinner.hideSpinner();
        this.toastr.error('La sala está llena');
      })
    );
    this.subscriptions.push(
      this.roomSrv.onRoomNotFound().subscribe((_) => {
        this.spinner.hideSpinner();
        this.toastr.error('No se ha encontrado la sala');
      })
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
    this.spinner.showSpinner();
    this.toastr.info('Uniéndose a la sala');
    const roomCode: string | undefined = this.getRoomCode();
    console.log('Joining with code:', roomCode);
    // Valido el código hexadecimal
    if (roomCode != undefined) this.roomSrv.joinRoom(roomCode);
  }

  onCreateRoom() {
    this.spinner.showSpinner();
    this.toastr.info('Creando una sala nueva...')
    this.roomSrv.createAndJoinRoom();
  }
}
