from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from setting.models import Country, City, Consultation, Speciality, InsuranceCompany


class SpecialitySerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name
        }

    class Meta:
        model = Speciality


class InsuranceCompanySerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name
        }

    class Meta:
        model = InsuranceCompany

class ConsultationSerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name
        }

    class Meta:
        model = Consultation

class CitySerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name
        }

    class Meta:
        model = City

class CountrySerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name,
            "cities": CitySerializer(instance.cities, many=True).data,
            "insuranceCompanies": InsuranceCompanySerializer(instance.insurance_companies, many=True).data
        }

    class Meta:
        model = Country
