import { Component, Input, OnInit } from '@angular/core';
import { Accusation } from 'src/app/interfaces/accusation';

@Component({
  selector: 'app-ingame-modal',
  templateUrl: './ingame-modal.component.html',
  styleUrls: ['./ingame-modal.component.scss'],
})
export class IngameModalComponent implements OnInit {
  @Input() subjectClass: string = 'player-color-2';
  @Input() accusation: Accusation = {
    developer: 'Juan',
    module: 'Nómina',
    error: 'SyntaxError',
  };

  constructor() {}

  ngOnInit(): void {}
}
