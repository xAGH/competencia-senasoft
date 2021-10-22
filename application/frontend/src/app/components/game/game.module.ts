import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayerBadgeComponent } from './player-badge/player-badge.component';
import { IngameModalComponent } from './ingame-modal/ingame-modal.component';
import { ChatViewComponent } from './chat-view/chat-view.component';
import { SharedModule } from '../shared/shared.module';
import { ChatMessageComponent } from './chat-message/chat-message.component';
import { CardSelectionComponent } from './card-selection/card-selection.component';



@NgModule({
  declarations: [
    PlayerBadgeComponent,
    IngameModalComponent,
    ChatViewComponent,
    ChatMessageComponent,
    CardSelectionComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,
  ],
  exports: [
    PlayerBadgeComponent,
    IngameModalComponent,
    ChatViewComponent,
    ChatMessageComponent,
    CardSelectionComponent,
  ]
})
export class GameModule { }
