import { Injectable } from '@angular/core';
import {
  Router,
  Resolve,
  RouterStateSnapshot,
  ActivatedRouteSnapshot,
} from '@angular/router';
import { Observable, of } from 'rxjs';
import { tap } from 'rxjs/operators';
import { RoomSessionService } from '../services/room-session.service';
import { RoomService } from '../services/room.service';

@Injectable({
  providedIn: 'root',
})
export class LobbyResolver implements Resolve<boolean> {
  constructor(
    private router: Router,
    private roomSrv: RoomService,
    private roomSessionSrv: RoomSessionService
  ) {}

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> {
    if (this.roomSessionSrv.info == undefined) return of(false);
    const roomCode = route.paramMap.get('code');
    // Si el código está indefinido, retorno
    if (roomCode == undefined) {
      this.router.navigateByUrl('home');
      return of(false);
    } else {
      return this.roomSrv.checkRoomExists(roomCode).pipe(
        tap((res: any) => {
          if (!res.exists) {
            this.router.navigateByUrl('home');
            return of(false);
          } else {
            return of(true);
          }
        })
      );
    }
  }
}
