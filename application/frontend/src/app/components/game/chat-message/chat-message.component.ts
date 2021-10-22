import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-chat-message',
  templateUrl: './chat-message.component.html',
  styleUrls: ['./chat-message.component.scss']
})
export class ChatMessageComponent implements OnInit {

  constructor() { }

  @Input() playerName: string = '';
  @Input() playerID : number = -1;
  @Input() message: string = '';
  @Input() isSystemMessage: boolean = false;

  ngOnInit(): void {
  }

  styleCodes : {[key: number]: string} = {
    0: 'player-color-1',
    1: 'player-color-2',
    2: 'player-color-3',
    3: 'player-color-4',
    999: 'error-color',
  }

  resolveClassStyle() : string {
    if(this.playerID in this.styleCodes) {
      return this.styleCodes[this.playerID];
    }else {
      return '';
    }
  }
}
