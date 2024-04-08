import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

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
}
