import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ClipboardService } from 'ngx-clipboard';
import { Subscription } from 'rxjs';
import { PlayerInfo } from 'src/app/interfaces/player-info';
import { RoomSessionService } from 'src/app/services/room-session.service';
import { RoomService } from 'src/app/services/room.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss'],
  host: { class: 'full-extent' },
})
export class LobbyComponent implements OnInit, OnDestroy {
  roomCode: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private roomSessionSrv: RoomSessionService,
    private roomSrv: RoomService,
    private cliboard: ClipboardService
  ) {}

  playerList: PlayerInfo[] = [];
  subscriptions: Subscription[] = [];

  ngOnInit(): void {
    this.roomCode = this.route.snapshot.paramMap.get('code');
    if (this.roomCode) {
      const playerList = this.roomSessionSrv.info;
      if (playerList?.users != undefined) this.playerList = playerList?.users;
      this.subscriptions.push(
        this.roomSrv.onJoinedRoom().subscribe((res) => {
          this.playerList = res.users;
        })
      );

      this.subscriptions.push(
        this.roomSrv.onLeftRoom().subscribe((res) => {
          this.playerList = res.users;
        })
      );
    } else {
      this.router.navigateByUrl('');
    }
  }

  onCopyRoomID() {
    if (this.roomCode != null) this.cliboard.copy(this.roomCode);
  }

  onLeaveLobby() {
    const user = this.roomSessionSrv.info?.you;
    if (user) {
      this.roomSrv.leaveRoom(user);
      this.roomSessionSrv.wipe();
    }
    this.router.navigateByUrl('home');
  }

  ngOnDestroy() {
    this.subscriptions.forEach((sub) => sub.unsubscribe());
  }
}
