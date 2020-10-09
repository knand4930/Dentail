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
    msg = models.TextField(default="Your Message", blank=True)

    def __str__(self):
        return self.name
    
