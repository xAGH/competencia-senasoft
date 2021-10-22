import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GameRoutingModule } from './game-routing.module';
import { GameComponent } from './game.component';
import { SharedModule } from '../../shared/shared.module';
import { GameModule } from '../../game/game.module';


@NgModule({
  declarations: [
    GameComponent
  ],
  imports: [
    CommonModule,
    GameRoutingModule,
    SharedModule,
    GameModule,
  ]
})
export class GameViewModule { }
