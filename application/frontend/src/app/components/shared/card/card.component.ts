import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class CardComponent implements OnInit {

  constructor() { }

  @Input() cardImgUrl: string = '';
  @Input() cardType : string = 'dev';
  @Input() cardTitle: string = 'CardTitle';
  @Input() reverse = false;
  @Input() selected = false;

  ngOnInit(): void {
  }

}
