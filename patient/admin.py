from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from django.utils.translation import gettext_lazy as _
from .models import Patient


@admin.register(Patient)
class PatientAdmin(TranslatedFieldAdmin, admin.ModelAdmin):

    search_fields = ("phone", "name", "id")
    autocomplete_fields = ('user', 'country', 'city')
