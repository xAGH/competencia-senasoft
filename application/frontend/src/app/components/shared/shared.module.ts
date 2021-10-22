import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from 'src/app/components/shared/card/card.component';
import { SpinnerComponent } from 'src/app/components/shared/spinner/spinner.component';
import { FooterComponent } from './footer/footer.component';
import { RouterModule } from '@angular/router';
import { HeadingComponent } from './heading/heading.component';

@NgModule({
  declarations: [
    CardComponent,
    SpinnerComponent,
    FooterComponent,
    HeadingComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: [
    CardComponent,
    SpinnerComponent,
    FooterComponent,
    HeadingComponent,
  ]
})
export class SharedModule { }
