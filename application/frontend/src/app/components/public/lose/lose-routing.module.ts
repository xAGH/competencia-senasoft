import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoseComponent } from './lose.component';

const routes: Routes = [{ path: '', component: LoseComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoseRoutingModule { }
