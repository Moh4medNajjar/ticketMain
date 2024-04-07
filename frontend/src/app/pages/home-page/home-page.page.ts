import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { EventService } from 'src/app/services/event.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.page.html',
  styleUrls: ['./home-page.page.scss'],
})
export class HomePagePage implements OnInit {

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

  @ViewChild('featuredContainer') featuredContainer!: ElementRef;

  scrollStep = 200; // Number of pixels to scroll per click




  scroll(direction: number): void {
    const container = this.featuredContainer.nativeElement;
    const scrollAmount = direction * this.scrollStep;
    container.scrollLeft += scrollAmount;
  }



}
