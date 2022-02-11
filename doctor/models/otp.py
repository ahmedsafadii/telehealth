from django.db import models
from django.utils.translation import gettext_lazy as _


class DoctorOTP(models.Model):
    country = models.ForeignKey("setting.Country", on_delete=models.CASCADE, related_name="doctor_otp",
                                blank=False, null=True, verbose_name=_("Country"))
    phone = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Phone"))
    code = models.CharField(max_length=6, blank=False, null=True, verbose_name=_("Code"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        unique_together = ("country", "phone")
        verbose_name_plural = _('Doctors OTP')
        verbose_name = _('Doctor OTP')

    def __str__(self):
        return self.phone
