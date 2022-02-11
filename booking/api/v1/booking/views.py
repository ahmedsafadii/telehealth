from rest_framework.views import APIView

from booking.models import Booking
from telehealth.middleware import json_response
from booking.api.v1.booking.serializer import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _


class MyBooking(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):  # noqa
        booking = Booking.objects.filter(doctor=request.user.doctor)
        booking_ser = BookingSerializer(booking, many=True, context={'request': request}).data
        return json_response(data=booking_ser)
