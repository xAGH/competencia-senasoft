import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WonComponent } from './won.component';

const routes: Routes = [{ path: '', component: WonComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WonRoutingModule { }
