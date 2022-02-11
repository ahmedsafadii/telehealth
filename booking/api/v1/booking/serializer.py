from rest_framework import serializers
from booking.models import Booking
from setting.api.v1.setting.serializer import ConsultationSerializer


class BookingSerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "consultationType": ConsultationSerializer(instance.consultation_type, many=False).data,
            "price": instance.price,
            "date": instance.date,
            "startTime": instance.start_time,
            "endTime": instance.end_time,
            "created": instance.created
        }

    class Meta:
        model = Booking