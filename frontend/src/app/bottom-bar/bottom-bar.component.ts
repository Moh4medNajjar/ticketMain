import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bottom-bar',
  templateUrl: './bottom-bar.component.html',
  styleUrls: ['./bottom-bar.component.scss'],
})
export class BottomBarComponent implements OnInit {
  activeIcon: string = '';

  constructor(private router: Router) { }

  ngOnInit() {}

  navigateToPage(pageUrl: string, icon: string): void {
    console.log(`Navigating to page: ${pageUrl} with icon: ${icon}`);

    // Update color based on current route URL
    const currentPageUrl = this.router.url;
    if (currentPageUrl !== pageUrl) {
      // Update color of all icons
      const icons = document.querySelectorAll('.icon');
      icons.forEach((element: Element) => {
        const iconName = element.getAttribute('name');
        if (iconName === icon) {
          element.classList.add('active');
        } else {
          element.classList.remove('active');
        }
      });

      // Update active icon
      this.activeIcon = icon;

      // Navigate only if not already on the page
      this.router.navigateByUrl(pageUrl);
    }
  }
}
