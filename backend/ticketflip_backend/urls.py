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
from django.contrib import admin
from django.urls import path, include
import feedback.views
from rating.views import rating_detail, rating_create, rating_update, rating_delete, rating_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', feedback.views.feedback_list, name='feedback_list'),
    path('feedback/create/', feedback.views.feedback_create, name='feedback_create'),
    path('feedback/<int:feedback_id>/', feedback.views.feedback_detail, name='feedback_detail'),
    path('feedback/<int:feedback_id>/update/', feedback.views.feedback_update, name='feedback_update'),
    path('feedback/<int:feedback_id>/delete/', feedback.views.feedback_delete, name='feedback_delete'),
    path('event/<int:event_id>/ratings/', rating_list, name='rating_list'),
    path('event/<int:event_id>/rating/<int:rating_id>/', rating_detail, name='rating_detail'),
    path('event/<int:event_id>/rating/create/', rating_create, name='rating_create'),
    path('event/<int:event_id>/rating/<int:rating_id>/update/', rating_update, name='rating_update'),
    path('event/<int:event_id>/rating/<int:rating_id>/delete/', rating_delete, name='rating_delete'),
    path('cart/', include('cart.urls')),
]
