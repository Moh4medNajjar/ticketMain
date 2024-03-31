import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-event-adding',
  templateUrl: './event-adding.page.html',
  styleUrls: ['./event-adding.page.scss'],
})
export class EventAddingPage {

  constructor() { }

  eventTitle!: string;
  aboutEvent!: string;
  imagePreview!: string;

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
      this.imagePreview = reader.result as string;
    };

    reader.readAsDataURL(file);
  }

  submitEvent() {
    // Implement your submit event logic here
    console.log('Submitting event...');
  }

  discardEvent() {
    // Implement your discard event logic here
    console.log('Discarding event...');
  }

}


