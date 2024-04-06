import { Component, OnInit } from '@angular/core';
import { EventService } from 'src/app/services/event.service';

@Component({
  selector: 'app-featuredevents',
  templateUrl: './featuredevents.page.html',
  styleUrls: ['./featuredevents.page.scss'],
})
export class FeaturedeventsPage implements OnInit {

  events: any[] = [];

  constructor(private eventService: EventService) { }

  ngOnInit(): void {
    this.fetchEvents();
  }

  fetchEvents(): void {
    this.eventService.getEvents()
      .subscribe(
        (events: any[]) => {
          this.events = events;
          console.log('Events:', this.events);
        },
        (error: any) => {
          console.error('Error fetching events:', error);
        }
      );
  }

}
