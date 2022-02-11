from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from .models import Doctor, DoctorConsultation, DoctorInsuranceCompany, DoctorTimeSlot
from django.utils.translation import gettext_lazy as _
from setting.models import Consultation, InsuranceCompany


class TimeSlotAdmin(TranslatedFieldAdmin, admin.TabularInline):
    extra = 1
    model = DoctorTimeSlot


class DoctorInsuranceCompanyAdmin(TranslatedFieldAdmin, admin.TabularInline):

    def get_max_num(self, request, obj=None, **kwargs):
        return InsuranceCompany.objects.all().count()

    autocomplete_fields = ('insurance_company',)
    extra = 1
    model = DoctorInsuranceCompany


class DoctorConsultationAdmin(TranslatedFieldAdmin, admin.TabularInline):

    def get_max_num(self, request, obj=None, **kwargs):
        return Consultation.objects.all().count()

    autocomplete_fields = ('consultation',)
    extra = 1
    model = DoctorConsultation


@admin.register(Doctor)
class DoctorAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    search_fields = ("phone", "id")
    autocomplete_fields = ('user', 'country', 'city', 'specialities')

    inlines = [
        DoctorConsultationAdmin,
        DoctorInsuranceCompanyAdmin,
        TimeSlotAdmin
    ]


@admin.register(DoctorTimeSlot)
class DoctorTimeSlotAdmin(admin.ModelAdmin):
    search_fields = ("start_time", "end_time")
    autocomplete_fields = ("doctor",)