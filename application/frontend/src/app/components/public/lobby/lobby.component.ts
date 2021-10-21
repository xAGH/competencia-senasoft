import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { PlayerInfo } from 'src/app/interfaces/player-info';
import { RoomSessionService } from 'src/app/services/room-session.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss'],
  host: { class: 'full-extent' },
})
export class LobbyComponent implements OnInit {
  roomCode: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private roomSessionSrv: RoomSessionService
  ) {}

  roomId: string = 'ABCDE';

  playerList: PlayerInfo[] = [];

  ngOnInit(): void {
    this.roomCode = this.route.snapshot.paramMap.get('code');
    if (this.roomCode) {
      const playerList = this.roomSessionSrv.info;
      if (playerList?.users != undefined) this.playerList = playerList?.users;
    } else {
      this.router.navigateByUrl('');
    }
  }
}
