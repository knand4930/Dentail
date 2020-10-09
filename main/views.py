from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Main, Appointment, AboutUs, Price, Contact


# Create your views here.

def home(request):
    settings = Main.objects.get(pk=1)
    about = AboutUs.objects.get(pk=1)
    prices = Price.objects.all()[:5]
    return render(request, 'home.html', {'settings': settings, 'about': about, 'prices': prices})


def contact(request):
    return render(request, 'contact.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        print(name)
        b = Contact(name=name, email=email, msg=msg)
        b.save()
    return redirect('contact')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        msg = request.POST.get('msg')
        b = Appointment(name=name, phone=phone, email=email, address=address, msg=msg)
        b.save()

    return redirect('home')


def price(request):
    prices = Price.objects.all()
    return render(request, 'pricing.html', {'prices': prices})
