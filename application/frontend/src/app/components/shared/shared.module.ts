import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from 'src/app/components/shared/card/card.component';
import { SpinnerComponent } from 'src/app/components/shared/spinner/spinner.component';
import { FooterComponent } from './footer/footer.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    CardComponent,
    SpinnerComponent,
    FooterComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: [
    CardComponent,
    SpinnerComponent,
    FooterComponent,
  ]
})
export class SharedModule { }
