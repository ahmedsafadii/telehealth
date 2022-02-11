from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from booking.models import Booking
from doctor.models import DoctorTimeSlot
from telehealth.middleware import json_response
from doctor.api.v1.doctor.serializer import SignUpSerializer, GetCodeSerializer, ProfileSerializer, SignInSerializer, \
    UpdateProfileSerializer, GetMyAvailableSlotSerializer
from django.utils.translation import gettext_lazy as _


class SignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):  # noqa
        signup_ser = SignUpSerializer(data=request.data, context={'request': request})
        if signup_ser.is_valid():
            return json_response(data=signup_ser.save())
        else:
            print("errors", signup_ser.errors)
            return json_response(message=_("Please fix the errors below"), errors=signup_ser.errors)


class SignIn(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):  # noqa
        signIn_ser = SignInSerializer(data=request.data, context={'request': request})
        if signIn_ser.is_valid():
            return json_response(data=signIn_ser.save())
        else:
            return json_response(message=_("Please fix the errors below"), errors=signIn_ser.errors)


class GetCode(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):  # noqa
        getcode_ser = GetCodeSerializer(data=request.data, context={'request': request})
        if getcode_ser.is_valid():
            return json_response(data=getcode_ser.save())
        else:
            return json_response(message=_("Please fix the errors below"), errors=getcode_ser.errors)


class Profile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):  # noqa
        profile_ser = ProfileSerializer(request.user).data
        return json_response(data=profile_ser)


class UpdateProfile(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):  # noqa

        update_profile_ser = UpdateProfileSerializer(data=request.data, context={'request': request})
        if update_profile_ser.is_valid():
            user = update_profile_ser.save()
            return json_response(data=user)
        else:
            return json_response(message=_("Please fix the errors below"), errors=update_profile_ser.errors)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):  # noqa
        request.user.auth_token.delete()
        return json_response()


class GetMyAvailableSlot(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):  # noqa
        bookings_times = list(Booking.objects.filter(doctor=request.user.doctor).values_list("time_id", flat=True))
        available_slots = request.user.doctor.slots.exclude(id__in=bookings_times)
        available_slots_serializer = GetMyAvailableSlotSerializer(available_slots, many=True)
        return json_response(data=available_slots_serializer.data)
