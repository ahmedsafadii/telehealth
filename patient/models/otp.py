from django.db import models
from django.utils.translation import gettext_lazy as _


class PatientOTP(models.Model):
    country = models.ForeignKey("setting.Country", on_delete=models.CASCADE, related_name="otp",
                                blank=False, null=True, verbose_name=_("Country"))
    phone = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Phone"))
    code = models.CharField(max_length=6, blank=False, null=True, verbose_name=_("Code"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Patients OTP')
        verbose_name = _('Patient OTP')

    def __str__(self):
        return self.phone
