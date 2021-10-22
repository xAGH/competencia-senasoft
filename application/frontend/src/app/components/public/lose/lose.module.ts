import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoseRoutingModule } from './lose-routing.module';
import { LoseComponent } from './lose.component';
import { SharedModule } from '../../shared/shared.module';


@NgModule({
  declarations: [
    LoseComponent
  ],
  imports: [
    CommonModule,
    LoseRoutingModule,
    SharedModule,
  ]
})
export class LoseModule { }
