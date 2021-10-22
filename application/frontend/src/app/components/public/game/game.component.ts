import { DOCUMENT } from '@angular/common';
import { Component, Inject, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { delay } from 'rxjs/operators';
import { ChatMessage } from 'src/app/interfaces/chat-message';
import { GameCard } from 'src/app/interfaces/game-card';
import { PlayerInfo } from 'src/app/interfaces/player-info';
import { UserRoomIdentity } from 'src/app/interfaces/user-room-identity';
import { CardInfoService } from 'src/app/services/card-info.service';
import { GameService } from 'src/app/services/game.service';
import { RoomSessionService } from 'src/app/services/room-session.service';
import { RoomService } from 'src/app/services/room.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss'],
  host: { class: 'full-extent' },
})
export class GameComponent implements OnInit, OnDestroy {
  constructor(
    private gameSrv: GameService,
    private roomSessionSrv: RoomSessionService,
    private roomSrv: RoomService,
    private cardInfoSrv: CardInfoService,
    private router: Router,
    @Inject(DOCUMENT) private document: any
  ) {
    this.document.body.classList.add('lock-scroll-x');
  }

  gamePlayers: PlayerInfo[] = [];
  playerCards: number[] = [];

  chatMessages: ChatMessage[] = [];
  currentPlayer : PlayerInfo;
  playerNumber: number = -1;
  playerName: string = '';

  showChat = false;

  showReverse = true;

  resolvePlayerName(id: number) {
    if (id == 999) return 'Servidor';
    return this.gamePlayers[id]?.name ?? 'Desconocido';
  }

  ngOnInit(): void {
    if (this.roomSessionSrv.info == undefined) {
      this.router.navigateByUrl('home');
      return;
    }
    this.roomSrv.requestRoomInfo({room: this.roomSrv.currentRoomCode});
    this.roomSrv.onGetRoomInfo().subscribe((data: any) => {
      this.roomSessionSrv.info.users = data.players;
      this.gamePlayers = data.players ?? [];
      this.currentPlayer = this.gamePlayers[this.gameSrv.currentTurn];
      const player = this.roomSessionSrv.info.you;
      this.playerNumber = this.gamePlayers.findIndex(
        (el) => el.sid == player.sid
      );
      this.playerName = player.name;
      this.playerCards = this.gameSrv.playerCards.map(el => el.id);
    });
    this.roomSrv.onMessage().subscribe((msgData: any) => {
      const player = msgData.player;
      const playerIndex = this.gamePlayers.findIndex(
        (el) => el.sid == player.sid
      );
      const isSystemMessage = msgData.system_message;
      this.playerNumber = playerIndex;
      this.chatMessages.push({
        playerID: isSystemMessage ? 999 : playerIndex,
        message: msgData.message,
        isSystemMessage: isSystemMessage,
      });
    });

    of(delay(4000)).subscribe(() => {
      this.showReverse = false;
    })
  }

  ngOnDestroy() {
    this.document.body.classList.remove('lock-scroll-x');
  }

  onChatOpen() {
    this.showChat = true;
  }

  onChatClose() {
    this.showChat = false;
  }

  onChatMessage(msg: string) {
    const you = this.roomSessionSrv.info?.you;
    const room = this.roomSrv.currentRoomCode;
    if (you == undefined || room == undefined) return;
    this.roomSrv.sendMessage({
      message: msg,
      player: you ?? undefined,
      room: room,
    });
  }

  getCardUrl(id: number) {
    return this.cardInfoSrv.getCardImageUrl(id);
  }

  getCardTitle(id: number) {
    return this.cardInfoSrv.getCardTitle(id);
  }

  getCardType(id: number) {
    return this.cardInfoSrv.getCardType(id);
  }
}
