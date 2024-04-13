import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {}
  private apiUrl = 'http://localhost:8000/api/users/';


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



  // deleteCartItem(userId: number, itemId: number) {
  //   const url = `${this.apiUrl}${userId}/`;

  //   const payload = {
  //     item_id: itemId
  //   };

  //   this.http.request('delete', url, {
  //     body: payload
  //   }).subscribe(
  //     (response: any) => {
  //       console.log(response); // Handle success response
  //       // Optionally, update the cart display or perform other actions
  //     },
  //     (error) => {
  //       console.error(error); // Handle error response
  //     }
  //   );
  // }

  deleteCartItem(user: any, itemId: number) {
    const url = `${this.apiUrl}${user.id}/`;
    console.log(user)

    let index = user.cart.indexOf(itemId);
    if (index !== -1) {
        user.cart.splice(index, 1);
    }
    console.log(user.cart)

    const payload = {
      user: user
    };

    this.http.request('put', url, {
      body: payload
    }).subscribe(
      (response: any) => {
        console.log(response); // Handle success response
        // Optionally, update the cart display or perform other actions
      },
      (error) => {
        console.error(error); // Handle error response
      }
    );
  }


  }
