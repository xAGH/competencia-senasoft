import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ClipboardModule } from 'ngx-clipboard';
import { SocketIoModule } from 'ngx-socket-io';
import { ToastrModule } from 'ngx-toastr';
import { environment } from 'src/environments/environment';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { SharedModule } from './components/shared/shared.module';
import { ApiInterceptor } from './interceptors/api.interceptor';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    RouterModule,
    SocketIoModule.forRoot({
      url: environment.websocket_endpoint,
      options: { autoConnect: false },
    }),
    HttpClientModule,
    ClipboardModule,
    ToastrModule.forRoot({
      closeButton: false,
      timeOut: 3000,
      easeTime: 100,
      maxOpened: 5,
      newestOnTop: true,
    }),
    BrowserAnimationsModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: ApiInterceptor, multi: true },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
