from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Main(models.Model):
    home_title = models.CharField(max_length=250, blank=True)
    home_description = models.TextField(default="None", blank=True)

    def __str__(self):
        return self.home_title


class AboutUs(models.Model):
    txt = models.TextField(default="Our About us")


class Appointment(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(default="Your address", blank=True)
    msg = models.TextField(default="-", blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    serive_name = models.CharField(max_length=220, blank=True)
    stage = models.IntegerField()
    prices = models.IntegerField()

    def __str__(self):
        return self.serive_name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    msg = models.TextField(default="-", blank=True)

    def __str__(self):
        return self.name
