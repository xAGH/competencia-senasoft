import { Injectable } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  CanActivate,
  Router,
  RouterStateSnapshot,
  UrlTree,
} from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { RoomService } from '../services/room.service';

@Injectable({
  providedIn: 'root',
})
export class LobbyGuard implements CanActivate {
  constructor(
    private router: Router,
    private route: ActivatedRouteSnapshot,
    private roomSrv: RoomService
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ):
    | Observable<boolean | UrlTree>
    | Promise<boolean | UrlTree>
    | boolean
    | UrlTree {
    const code = this.route.queryParamMap.get('code');
    // Si no me entregaron un código de sala
    if (code == null) return this.router.parseUrl('home');
    return this.roomSrv.checkRoomExists(code).pipe(tap((res: any) => {
      return res.exists;
    }));
  }
}
