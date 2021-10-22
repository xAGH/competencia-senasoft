import { Component, ElementRef, OnInit, Output, ViewChild } from '@angular/core';
import { EventEmitter } from '@angular/core';

@Component({
  selector: 'app-chat-view',
  templateUrl: './chat-view.component.html',
  styleUrls: ['./chat-view.component.scss']
})
export class ChatViewComponent implements OnInit {

  constructor() { }

  @Output() close = new EventEmitter();
  @Output() send = new EventEmitter<string>()

  @ViewChild('messageInput') messageInput?: ElementRef;

  ngOnInit(): void {
  }

  emitClose() {
    this.close.emit();
  }

  emitSend() {
    if(this.messageInput == undefined) return;
    const value = this.messageInput?.nativeElement.value;
    this.messageInput.nativeElement.value = '';
    this.send.emit(value);
  }

}
