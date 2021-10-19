import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { SpinnerService } from '../services';
import { finalize } from 'rxjs/operators';

@Injectable()
export class ApiInterceptor implements HttpInterceptor {

  private readonly apiUrl: string = environment.BASE_URL;

  constructor(private spinnerService: SpinnerService) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.spinnerService.showSpinner();
    request.clone({
      url: `${this.apiUrl}/${request.url}`,
      withCredentials: true,
    })
    return next.handle(request).pipe(
      finalize(() => this.spinnerService.hideSpinner())
    );
  }
}
