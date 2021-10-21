import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-hall',
  templateUrl: './hall.component.html',
  styleUrls: ['./hall.component.scss'],
  host: {'class': 'full-extent'}
})
export class HallComponent implements OnInit {

  @ViewChild('roomInput') roomInput? : ElementRef;

  constructor() { }

  ngOnInit(): void {
  }

  validCode = false;

  private getRoomCode() : string | undefined{
    return this.roomInput?.nativeElement.value ?? undefined;
  }

  onJoinRoom() {
    const roomCode : string | undefined = this.getRoomCode()
    console.log('Joining with code:', roomCode);
    const regex = /[0-9A-F]{5}$/i;
    // Valido el código hexadecimal
    this.validCode = roomCode != undefined && regex.test(roomCode);
    if (this.validCode){
      console.log('VALID!')
    }
  }

  onCreateRoom() {
    console.log('Creating')
  }

}
