import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GameService {

 constructor() { }

 hiddenCards : any[] = []
 playerCards: any[] = []
 discoveredCards: any[] = []
 currentTurn : number = 0;
}
