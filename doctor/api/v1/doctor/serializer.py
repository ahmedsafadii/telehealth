from rest_framework import serializers
from rest_framework.throttling import UserRateThrottle
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from setting.api.v1.setting.serializer import SpecialitySerializer, ConsultationSerializer
from setting.models import Country, Consultation, InsuranceCompany, Speciality
from doctor.models import DoctorOTP, Doctor, DoctorConsultation, DoctorInsuranceCompany, DoctorTimeSlot
from random import randint

from telehealth.services.token import get_token


class SignUpSerializer(serializers.Serializer):  # noqa
    gender = serializers.ChoiceField(choices=Doctor.GENDER_CHOICES, required=True,
                                     allow_blank=False, allow_null=False)
    phone = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False, allow_null=False)
    country = serializers.IntegerField(required=True, allow_null=False)
    firstName = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False, allow_null=False)
    lastName = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False, allow_null=False)
    email = serializers.EmailField(required=True,
                                   allow_blank=False,
                                   allow_null=False,
                                   validators=[UniqueValidator(queryset=User.objects.all())])

    otpCode = serializers.CharField(max_length=255, min_length=6, required=True,
                                    allow_blank=False, allow_null=False)

    def validate_country(self, value):  # noqa
        try:
            Country.objects.get(id=value)
            return value
        except Country.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this country is not exist"))

    def validate(self, data):
        username = "D-" + str(data.get("phone")) + "-" + str(data.get("country"))

        try:
            code_object, code_created = DoctorOTP.objects.update_or_create(country_id=data.get('country'),
                                                                           phone=data.get('phone'),
                                                                           code=data.get('otpCode'))
            code_object.delete()
        except DoctorOTP.DoesNotExist:
            raise serializers.ValidationError({"otpCode": _("You enter a wrong code")})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"phone": _("This phone number is already exist")})

        return data

    def save(self, **kwargs):
        username = "D-" + str(self.validated_data.get("phone")) + "-" + str(self.validated_data.get("country"))

        user_object, user_created = User.objects.update_or_create(username=username)
        user_object.first_name = self.validated_data.get("firstName")
        user_object.last_name = self.validated_data.get("lastName")
        user_object.email = self.validated_data.get("email")
        user_object.save()

        doctor_object, doctor_created = Doctor.objects.update_or_create(user=user_object)
        doctor_object.gender = self.validated_data.get("gender")
        doctor_object.name_ar = self.validated_data.get("firstName") + " " + self.validated_data.get("lastName")
        doctor_object.name_en = self.validated_data.get("firstName") + " " + self.validated_data.get("lastName")
        doctor_object.name_ro = self.validated_data.get("firstName") + " " + self.validated_data.get("lastName")

        doctor_object.phone = self.validated_data.get("phone")
        doctor_object.country_id = self.validated_data.get("country")
        doctor_object.save()
        return ProfileSerializer(user_object, many=False).data


class SignInSerializer(serializers.Serializer):  # noqa
    phone = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False, allow_null=False)
    country = serializers.IntegerField(required=True, allow_null=False)
    otpCode = serializers.CharField(max_length=255, min_length=6, required=True,
                                    allow_blank=False, allow_null=False)

    def validate_country(self, value):  # noqa
        try:
            Country.objects.get(id=value)
            return value
        except Country.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this country is not exist"))

    def validate(self, data):
        try:
            code_object = DoctorOTP.objects.get(country_id=data.get('country'),
                                                phone=data.get('phone'),
                                                code=data.get('otpCode'))
            code_object.delete()
        except DoctorOTP.DoesNotExist:
            raise serializers.ValidationError({"otpCode": _("You enter a wrong code")})

        username = "D-" + str(data.get("phone")) + "-" + str(data.get("country"))

        user = User.objects.filter(username=username)
        if user.exists():
            data["user"] = user.first()
        else:
            raise serializers.ValidationError({"phone": _("This phone number is not register in our system")})

        return data

    def save(self, **kwargs):
        return ProfileSerializer(self.validated_data.get("user"), many=False).data


class OTPMinThrottle(UserRateThrottle):
    scope = 'otp_in_min'


class OTPHourThrottle(UserRateThrottle):
    scope = 'otp_in_hour'


class GetCodeSerializer(serializers.Serializer):  # noqa
    phone = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False, allow_null=False)
    country = serializers.IntegerField(required=True, allow_null=False)

    throttle_classes = [
        OTPMinThrottle,
        OTPHourThrottle
    ]

    def validate_country(self, value):  # noqa
        try:
            Country.objects.get(id=value)
            return value
        except Country.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this country is not exist"))

    def save(self, **kwargs):
        doctor_object, doctor_created = DoctorOTP.objects.update_or_create(country_id=self.validated_data["country"],
                                                                           phone=self.validated_data["phone"])

        code = randint(100000, 999999)
        doctor_object.code = code
        doctor_object.save()

        # Warning: this should be removed in the future
        return {
            "code": code
        }


class DoctorConsultationSerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "consultation": {
                'id': instance.consultation.id,
                'name': instance.consultation.name
            },
            "price": instance.price
        }

    class Meta:
        model = DoctorConsultation


class DoctorInsuranceCompanySerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "insuranceCompany": {
                'id': instance.insurance_company.id,
                'name': instance.insurance_company.name
            },
            "number": instance.number
        }

    class Meta:
        model = DoctorConsultation


class ProfileSerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):
        data = {
            "userId": instance.id,
            "doctorId": instance.doctor.id,
            "address": instance.doctor.address,
            "bio": instance.doctor.bio,
            "gender": {
                "id": instance.doctor.gender,
                "title": instance.doctor.get_gender_display()
            },
            "firstName": instance.first_name,
            "lastName": instance.last_name,
            "email": instance.email,
            "specialties": SpecialitySerializer(instance.doctor.specialities, many=True).data,
            "consultations": DoctorConsultationSerializer(instance.doctor.consultations, many=True).data,
            "insuranceCompanies": DoctorInsuranceCompanySerializer(instance.doctor.insurance_companies, many=True).data,
            "token": get_token(instance)
        }
        return data

    class Meta:
        model = User


class UpdateProfileSerializer(serializers.Serializer):  # noqa
    gender = serializers.ChoiceField(choices=Doctor.GENDER_CHOICES, required=False,
                                     allow_blank=True, allow_null=True)
    firstName = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    lastName = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    city = serializers.IntegerField(required=True, allow_null=False)
    consultationType = serializers.IntegerField(required=True, allow_null=False)
    consultationPrice = serializers.FloatField(required=True, allow_null=False)
    insuranceCompany = serializers.IntegerField(required=True, allow_null=False)
    insuranceNumber = serializers.CharField(max_length=255, min_length=4, required=True, allow_blank=False,
                                            allow_null=False)
    specialities = serializers.ListField(required=True, allow_null=False)

    def validate_consultationType(self, value):  # noqa
        try:
            Consultation.objects.get(id=value)
            return value
        except Consultation.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this consultation type is not exist"))

    def validate_insuranceCompany(self, value):  # noqa
        try:
            InsuranceCompany.objects.get(id=value)
            return value
        except InsuranceCompany.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this company is not exist"))

    def validate_country(self, value):  # noqa
        try:
            Country.objects.get(id=value)
            return value
        except Country.DoesNotExist:
            raise serializers.ValidationError(_("Looks like this country is not exist"))

    def validate(self, data):

        specialities = Speciality.objects.filter(id__in=data['specialities'])

        if specialities.count() < len(data['specialities']):
            raise serializers.ValidationError({"specialities": _("Looks like some of specialities is not exist")})

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.first_name = self.validated_data['firstName']
        user.last_name = self.validated_data['lastName']
        user.doctor.gender = self.validated_data['gender']
        user.doctor.address = self.validated_data['address']
        user.doctor.bio = self.validated_data['bio']
        user.doctor.specialities.set(self.validated_data['specialities'])
        user.save()

        dc_object, dc_created = DoctorConsultation.objects.update_or_create(doctor=user.doctor,
                                                                            consultation_id=self.validated_data['consultationType'])
        dc_object.price = self.validated_data['consultationPrice']
        dc_object.save()

        di_object, di_created = DoctorInsuranceCompany.objects.update_or_create(doctor=user.doctor,
                                                                                insurance_company_id=self.validated_data['insuranceCompany'])
        di_object.number = self.validated_data['insuranceNumber']
        di_object.save()

        return ProfileSerializer(user, many=False).data


class GetMyAvailableSlotSerializer(serializers.Serializer):  # noqa

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "price": instance.start_time,
            "date": instance.end_time,
            "startTime": instance.is_free,
            "endTime": instance.note,
            "created": instance.created
        }

    class Meta:
        model = DoctorTimeSlot

