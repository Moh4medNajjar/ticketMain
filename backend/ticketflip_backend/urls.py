"""ticketflip_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from user.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from django.urls import path
from event import views as event_views
from booking import views as booking_views
from ticket import views as ticket_views

urlpatterns = [
    path('api/users', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('events/', event_views.event_list, name='event_list'),
    path('events/<int:pk>/', event_views.event_detail, name='event_detail'),
    path('bookings/', booking_views.booking_list, name='booking_list'),
    path('bookings/<int:pk>/', booking_views.booking_detail, name='booking_detail'),
    path('tickets/', ticket_views.ticket_list, name='ticket_list'),
    path('tickets/<int:pk>/', ticket_views.ticket_detail, name='ticket_detail'),
]




