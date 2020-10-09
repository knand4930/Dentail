from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('price/', views.price, name='price'),
    path('appointment/', views.appointment, name='appointment'),
]