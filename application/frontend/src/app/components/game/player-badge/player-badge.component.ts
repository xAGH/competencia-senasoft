import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-player-badge',
  templateUrl: './player-badge.component.html',
  styleUrls: ['./player-badge.component.scss']
})
export class PlayerBadgeComponent implements OnInit {

  constructor() { }

  @Input() playerName: string = 'Jugador';
  @Input() playerNumber: number = 0;

  ngOnInit(): void {
  }

}
