import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HallRoutingModule } from './hall-routing.module';
import { HallComponent } from './hall.component';
import { SharedModule } from '../../shared/shared.module';


@NgModule({
  declarations: [
    HallComponent
  ],
  imports: [
    CommonModule,
    HallRoutingModule,
    SharedModule,
  ]
})
export class HallModule { }
