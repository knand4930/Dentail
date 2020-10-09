from django.contrib import admin
from .models import Main, Appointment, AboutUs, Price, Contact


# Register your models here.


class MainAdmin(admin.ModelAdmin):
    list_display = ['home_title']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Main, MainAdmin)

admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(AboutUs)

admin.site.register(Price)

admin.site.register(Contact, ContactAdmin)
