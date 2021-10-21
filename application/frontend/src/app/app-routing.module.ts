import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LobbyResolver } from './resolvers/lobby.resolver';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: 'home',
    loadChildren: () =>
      import('./components/public/home/home.module').then((m) => m.HomeModule),
  },
  {
    path: 'hall',
    loadChildren: () =>
      import('./components/public/hall/hall.module').then((m) => m.HallModule),
  },
  {
    path: 'lobby',
    loadChildren: () =>
      import('./components/public/lobby/lobby.module').then(
        (m) => m.LobbyModule
      ),
    resolve: {
      roomInfo: LobbyResolver,
    },
  },
  {
    path: '**',
    loadChildren: () =>
      import('./components/public/page-not-found/page-not-found.module').then(
        (m) => m.PageNotFoundModule
      ),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
