from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from setting.models import Country, Consultation, Speciality
from telehealth.middleware import json_response
from setting.api.v1.setting.serializer import CountrySerializer, ConsultationSerializer, SpecialitySerializer
from django.utils.translation import gettext_lazy as _


class Tools(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):  # noqa
        countries = CountrySerializer(Country.objects.all(), many=True)
        consultations = ConsultationSerializer(Consultation.objects.all(), many=True)
        specialties = SpecialitySerializer(Speciality.objects.all(), many=True)

        data = {
            'countries': countries.data,
            'consultations': consultations.data,
            'specialties': specialties.data
        }

        return json_response(data=data)




