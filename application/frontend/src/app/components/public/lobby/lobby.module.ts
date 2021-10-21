import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LobbyRoutingModule } from './lobby-routing.module';
import { LobbyComponent } from './lobby.component';
import { SharedModule } from '../../shared/shared.module';
import { GameModule } from '../../game/game.module';


@NgModule({
  declarations: [
    LobbyComponent
  ],
  imports: [
    CommonModule,
    LobbyRoutingModule,
    SharedModule,
    GameModule
  ]
})
export class LobbyModule { }
