import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-instructions',
  templateUrl: './instructions.component.html',
  styleUrls: ['./instructions.component.scss'],
  host: {'class': 'full-extent'},
})
export class InstructionsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
