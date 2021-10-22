import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

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
  },
  {
    path: 'game',
    loadChildren: () =>
      import('./components/public/game/game-view.module').then((m) => m.GameViewModule),
  },
  { path: 'won', loadChildren: () => import('./components/public/won/won.module').then(m => m.WonModule) },
  { path: 'lose', loadChildren: () => import('./components/public/lose/lose.module').then(m => m.LoseModule) },
  { path: 'instructions', loadChildren: () => import('./components/public/instructions/instructions.module').then(m => m.InstructionsModule) },
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
