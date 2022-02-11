from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    autocomplete_fields = ("doctor", 'patient', 'consultation_type', 'time')
