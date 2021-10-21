import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.scss'],
  host: {'class': 'full-extent'}
})
export class LobbyComponent implements OnInit {

  constructor() { }

  roomId : string = 'ABCDE';

  playerList = [
    "AAA",
    "BBB",
    "AAA",
    "BBB",
  ];

  ngOnInit(): void {
  }

}
