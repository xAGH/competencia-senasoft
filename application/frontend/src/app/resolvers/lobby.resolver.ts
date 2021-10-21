import { Injectable } from '@angular/core';
import {
  Router, Resolve,
  RouterStateSnapshot,
  ActivatedRouteSnapshot
} from '@angular/router';
import { Observable, of } from 'rxjs';
import { RoomService } from '../services/room.service';

@Injectable({
  providedIn: 'root'
})
export class LobbyResolver implements Resolve<boolean> {

  constructor(private router: Router, private roomSrv: RoomService) {
  }

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
    const roomCode = route.paramMap.get('code');
    // Si el código está indefinido, retorno
    if (roomCode == undefined) {
      this.router.navigateByUrl('home')
    }
    return of(true);
  }
}
