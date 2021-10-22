import { Component, Input, OnInit } from '@angular/core';
import { CardStoredData } from 'src/app/interfaces/card-stored-data';
import { GameCard } from 'src/app/interfaces/game-card';
import { PlayerInfo } from 'src/app/interfaces/player-info';
import { CardInfoService } from 'src/app/services/card-info.service';

@Component({
  selector: 'app-card-selection',
  templateUrl: './card-selection.component.html',
  styleUrls: ['./card-selection.component.scss'],
})
export class CardSelectionComponent implements OnInit {
  constructor(private cardInfoSrv: CardInfoService) {}

  private _cards: number[];

  @Input('cards')
  set cards(ids: number[]) {
    this.buildDetails(ids);
    this._cards = ids;
  }

  get cards() {
    return this._cards;
  }

  cardDetails: CardStoredData[] = [];
  selectTable: { [key: number]: boolean } = {};

  @Input() allowOnlyOne: boolean = false;

  ngOnInit(): void {}

  markSelected(i: number) {
    if (this.allowOnlyOne) {
      for (let key in this.selectTable) {
        this.selectTable[key] = false;
      }
      this.selectTable[i] = true;
    } else {
      this.selectTable[i] = !this.selectTable[i];
    }
  }

  buildDetails(ids: number[]) {
    for (let id of ids) {
      this.cardDetails.push(this.cardInfoSrv.getCardInfo(id));
      this.selectTable[id] = false;
    }
  }
}
