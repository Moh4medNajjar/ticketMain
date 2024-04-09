import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { EventService } from 'src/app/services/event.service';
import { UserService } from 'src/app/services/user.service';
<<<<<<< HEAD

=======
>>>>>>> 17aa69ceae612193bbd728175ccdc4684252d9f4
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.page.html',
  styleUrls: ['./home-page.page.scss'],
  providers: [UserService]
})
export class HomePagePage implements OnInit {

  userData: any;
  events: any[] = [];
<<<<<<< HEAD
  constructor(private eventService: EventService, private router:Router, private userService: UserService) { }

=======
  constructor(private eventService: EventService, private router:Router, public UserService: UserService) { }
  public userId = this.UserService.getUserDataFromToken();
>>>>>>> 17aa69ceae612193bbd728175ccdc4684252d9f4
  ngOnInit(): void {
    console.log('User ID:', this.userId);
    this.fetchEvents();
    this.userData = this.userService.getUserDataFromToken();
    console.log(this.userData); // Output user data to console for testing
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





  navigateToEventDetails(eventId: number) {
    this.router.navigate(['/event-details', eventId]); // Navigate to event-details page with event ID
  }




}
