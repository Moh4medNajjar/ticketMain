import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {}
  baseUrl= "localhost:8000/users"


  getUserDataFromToken(){
    const token = localStorage.getItem('token')
    if (!token) {
      console.log("Token not found")
    } else {
      try{
        let data = JSON.parse(window.atob(token.split('.')[1]))
        return data
      } catch (error) {
        console.error('Error parsing token:', error);
    }
    }
  }

  removeFromCart(userId: number, eventId: number): Observable<any> {
    const url = `${this.baseUrl}/${userId}`;
    return this.http.delete(url);
  }

  }
