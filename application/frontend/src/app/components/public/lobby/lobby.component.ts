import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ClipboardService } from 'ngx-clipboard';
import { Subscription } from 'rxjs';
import { PlayerInfo } from 'src/app/interfaces/player-info';
import { GameService } from 'src/app/services/game.service';
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
    private cliboard: ClipboardService,
    private gameSrv: GameService
  ) {}

  playerList: PlayerInfo[] = [];
  subscriptions: Subscription[] = [];
  isOwner = false;

  ngOnInit(): void {
    this.roomCode = this.route.snapshot.queryParamMap.get('code');
    if (this.roomCode) {
      const playerList = this.roomSessionSrv.info;
      if (playerList?.users == undefined) {
        this.router.navigateByUrl('home');
        return
      }

      this.playerList = playerList?.users;
      this.isOwner = this.roomSrv.getSocketID() == this.playerList[0].sid;
      this.subscriptions.push(
        this.roomSrv.onJoinedRoom().subscribe((res) => {
          this.playerList = res.users;
          this.isOwner = this.roomSrv.getSocketID() == this.playerList[0].sid;
        })
      );

      this.subscriptions.push(
        this.roomSrv.onLeftRoom().subscribe((res) => {
          this.playerList = res.users;
          this.isOwner = this.roomSrv.getSocketID() == this.playerList[0].sid;
        })
      );

      this.subscriptions.push(
        this.roomSrv.onGameStart().subscribe((res) => {
          this.gameSrv.currentTurn = res.turn;
          const player_index = this.playerList.findIndex(
            (el) => el.sid == this.roomSessionSrv.info?.you.sid
          );
          this.gameSrv.playerCards = res.data.player_cards[player_index];
          this.gameSrv.hiddenCards = res.data.hidden_cards;
          this.gameSrv.currentTurn = res.firstTurn;
          this.router.navigateByUrl('game');
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

  onStartGame() {
    if (this.roomCode != null) this.roomSrv.startGame(this.roomCode);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((sub) => sub.unsubscribe());
  }
}
