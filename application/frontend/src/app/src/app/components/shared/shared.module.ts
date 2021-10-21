import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from 'src/app/components/shared/card/card.component';
import { SpinnerComponent } from 'src/app/components/shared/spinner/spinner.component';

@NgModule({
  declarations: [
    CardComponent,
    SpinnerComponent,
  ],
  imports: [
    CommonModule,
  ],
  exports: [
    CardComponent,
    SpinnerComponent,
  ]
})
export class SharedModule { }
