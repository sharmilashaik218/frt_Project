
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contactus/', views.contactus, name='contactus'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]