import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayerBadgeComponent } from './player-badge/player-badge.component';



@NgModule({
  declarations: [
    PlayerBadgeComponent,
  ],
  imports: [
    CommonModule,
  ],
  exports: [
    PlayerBadgeComponent,
  ]
})
export class GameModule { }
