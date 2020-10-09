from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Main, Appointment, AboutUs


# Create your views here.

def home(request):
    settings = Main.objects.get(pk=1)
    about = AboutUs.objects.get(pk=1)
    return render(request, 'home.html', {'settings': settings, 'about':about})


def contact(request):
    return render(request, 'contact.html')



