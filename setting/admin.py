from django.contrib import admin
from .models import Country, City, InsuranceCompany, Consultation, Speciality
from translated_fields import TranslatedFieldAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Country)
class CountryAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    search_fields = ('name_en', 'name_ar', 'name_ro')

    fieldsets = (
        (_("Name Translate Fields"), {
            'classes': ('collapse',),
            "fields": Country.name.fields
        }),
        (None, {
            'fields': ('code',)
        }),
    )


@admin.register(City)
class CityAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    autocomplete_fields = ('country', )
    search_fields = ('name_en', 'name_ar', 'name_ro')

    fieldsets = (
        (_("Name Translate Fields"), {
            'classes': ('collapse',),
            "fields": City.name.fields
        }),
        (None, {
            'fields': ('country',)
        })
    )


@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    autocomplete_fields = ('country', )
    search_fields = ('name_en', 'name_ar', 'name_ro')

    fieldsets = (
        (_("Name Translate Fields"), {
            'classes': ('collapse',),
            "fields": InsuranceCompany.name.fields
        }),
        (None, {
            'fields': ('country',)
        })
    )


@admin.register(Consultation)
class ConsultationAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    search_fields = ('name_en', 'name_ar', 'name_ro')

    fieldsets = (
        (_("Name Translate Fields"), {
            'classes': ('collapse',),
            "fields": Consultation.name.fields
        }),
    )


@admin.register(Speciality)
class SpecialityAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    search_fields = ('name_en', 'name_ar', 'name_ro')

    fieldsets = (
        (_("Name Translate Fields"), {
            'classes': ('collapse',),
            "fields": Speciality.name.fields
        }),
    )
