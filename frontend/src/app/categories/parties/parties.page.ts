import { Component, OnInit } from '@angular/core';
import { EventService } from 'src/app/services/event.service';

@Component({
  selector: 'app-parties',
  templateUrl: './parties.page.html',
  styleUrls: ['./parties.page.scss'],
})
export class PartiesPage implements OnInit {

  events: any[] = [];

  constructor(private eventService: EventService) { }

  ngOnInit(): void {
    this.fetchPartiesEvents();
  }

  fetchPartiesEvents(): void {
    this.eventService.getEventsByCategory('parties')
      .subscribe(
        (events: any[]) => {
          this.events = events;
        },
        (error: any) => {
          console.error('Error fetching parties events:', error);
        }
      );
  }

}
