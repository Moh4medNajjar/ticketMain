import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://localhost:8000/api/auth/'; // Replace this with your Django backend URL

  constructor(private http: HttpClient) { }

  login(credentials: { username: string, password: string }): Observable<any> {
    return this.http.post<any>('http://localhost:8000/api/auth/login', credentials);
  }

  register(userData: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}register/`, userData);
  }

  logout(): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}logout/`, {});
  }

  getUserStatus(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}user/status/`);
  }
  
}
