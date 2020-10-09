from django.contrib import admin
from .models import Main, Appointment, AboutUs


# Register your models here.


class MainAdmin(admin.ModelAdmin):
    list_display = ['home_title']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


admin.site.register(Main, MainAdmin)

admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(AboutUs)
