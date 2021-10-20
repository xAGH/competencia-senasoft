import { Component, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { SpinnerService } from 'src/app/services/spinner.service';

@Component({
  selector: 'app-spinner',
  template: '<div></div>',
  styleUrls: ['./spinner.component.scss']
})
export class SpinnerComponent implements OnInit {

  public isLoarding$: Subject<boolean> = this.spinnerService.isLoading$;

  constructor(private spinnerService: SpinnerService) { }

  ngOnInit(): void {
  }

}
