
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  loginForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router :Router
  ) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

loginUser() {
  console.log('Login button clicked');
  console.log('Form validity:', this.loginForm.valid);
  if (this.loginForm.valid) {
    this.authService.login(this.loginForm.value).subscribe(
      response => {
        console.log('Login successful', response);
        console.log('is admin :',response.is_admin);
        localStorage.setItem('token', response.token); // Store token in local storage
        if(response.is_admin){
          this.router.navigate(['./super-user']);
        }
        else{
          this.router.navigate(['./home-page']);
        }
      },
      error => {
        console.error('Login failed', error);
        // Handle login error, e.g., display error message
      }
    );
  }
}

}
