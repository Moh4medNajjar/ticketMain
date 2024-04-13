import { Component, OnInit } from '@angular/core';
import { EventService } from 'src/app/services/event.service';
import { UserService } from 'src/app/services/user.service';

interface CartEvent {
  id: number; // Unique identifier for the event
  title: string;
  imageUrl: string;
  ticket_unit_price: number;
  available_tickets: number;
  selectedTickets: number;
}

@Component({
  selector: 'app-event-booking',
  templateUrl: './event-booking.page.html',
  styleUrls: ['./event-booking.page.scss'],
})
export class EventBookingPage implements OnInit {

  userId: any;
  userCart: any;
  cartEvents: CartEvent[] = [];
  user!: any;
  constructor(private userService: UserService, private eventService: EventService) { }

  ngOnInit(): void {
    this.user = this.userService.getUserDataFromToken();
    this.userId = this.userService.getUserDataFromToken().id;
    this.userCart = this.userService.getUserDataFromToken().cart;

    this.loadCartEvents();
  }

  loadCartEvents(): void {
    this.cartEvents = [];
    this.userCart.forEach((eventId: number) => {
      this.eventService.getEventDetails(eventId).subscribe(
        (eventDetails: any) => {
          const cartEvent: CartEvent = {
            id: eventDetails.id,
            title: eventDetails.title,
            imageUrl: '../../../../assets/ev4.png', // Example image URL
            ticket_unit_price: eventDetails.ticket_unit_price,
            available_tickets: eventDetails.available_tickets,
            selectedTickets: 0, // Initialize selectedTickets to 0
          };
          this.cartEvents.push(cartEvent);
        },
        (error: any) => {
          console.error('Error fetching event details:', error);
        }
      );
    });
  }

  incrementTickets(event: CartEvent): void {
    if (event.selectedTickets < event.available_tickets) {
      event.selectedTickets++;
    }
  }

  decrementTickets(event: CartEvent): void {
    if (event.selectedTickets > 0) {
      event.selectedTickets--;
    }
  }

  calculateTotalPrice(event: CartEvent): number {
    return event.selectedTickets * event.ticket_unit_price;
  }

  calculateGrandTotal(): number {
    return this.cartEvents.reduce((total, event) => total + this.calculateTotalPrice(event), 0);
  }

  onDeleteItem(itemId: number): void {
    this.userService.deleteCartItem(this.user, itemId)
  }

}
