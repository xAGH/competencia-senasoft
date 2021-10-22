import { Component, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { SpinnerService } from 'src/app/services/spinner.service';

@Component({
  selector: 'app-spinner',
  template: `<div *ngIf="this.spinnerService.isLoading$ | async" class="game-card-container">
    <img class="game-card" src="assets/cards/Card.png" alt="">
  </div>`,
  styleUrls: ['./spinner.component.scss']
})
export class SpinnerComponent implements OnInit {

  public isLoarding$: Subject<boolean> = this.spinnerService.isLoading$;

  constructor(public spinnerService: SpinnerService) { }

  ngOnInit(): void {
  }

}
