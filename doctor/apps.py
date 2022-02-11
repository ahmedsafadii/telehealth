from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DoctorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor'
    verbose_name = _("Doctors")
