from booking.api.v1.booking import views
from django.urls import path

urlpatterns = [
    path('get_my_bookings', views.MyBooking.as_view())
]
