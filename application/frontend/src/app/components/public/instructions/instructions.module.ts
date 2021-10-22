import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { InstructionsRoutingModule } from './instructions-routing.module';
import { InstructionsComponent } from './instructions.component';
import { SharedModule } from '../../shared/shared.module';


@NgModule({
  declarations: [
    InstructionsComponent
  ],
  imports: [
    CommonModule,
    InstructionsRoutingModule,
    SharedModule,
  ]
})
export class InstructionsModule { }
