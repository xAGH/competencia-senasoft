import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hall',
  templateUrl: './hall.component.html',
  styleUrls: ['./hall.component.scss'],
  host: {'class': 'full-extent'}
})
export class HallComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  onJoinRoom() {
    console.log('Joining')
  }

  onCreateRoom() {
    console.log('Creating')
  }

}
