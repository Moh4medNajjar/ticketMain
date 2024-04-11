import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  private eventsUrl = 'http://localhost:8000/events/';
  private apiUrl = 'http://localhost:8000/events';


  constructor(private http: HttpClient) { }

  getEvents(): Observable<any[]> {
    return this.http.get<any[]>(this.eventsUrl);
  }

  getEventsByCategory(category: string): Observable<any[]> {
    const url = `${this.apiUrl}?category=${category}`;
    return this.http.get<any[]>(url);
  }

  getEventDetails(eventId: number): Observable<any> {
    const url = `${this.apiUrl}/${eventId}/`;
    return this.http.get<any>(url);
  }
}
