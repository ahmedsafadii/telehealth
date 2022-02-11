from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient",
                                blank=False, null=False, verbose_name=_("User"))
    name = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Name"))

    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    gender = models.CharField(max_length=1, null=True, blank=False, choices=GENDER_CHOICES)

    picture = models.ImageField(upload_to="doctors/profile_pictures", blank=True, null=True, verbose_name=_("Picture"))

    country = models.ForeignKey("setting.Country", on_delete=models.CASCADE, related_name="patients",
                                blank=False, null=True, verbose_name=_("Country"))

    city = models.ForeignKey("setting.City", on_delete=models.CASCADE, related_name="patients",
                             blank=False, null=True, verbose_name=_("City"))

    phone = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Phone"))

    address = models.TextField(blank=False, null=True, verbose_name=_("Address"))

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Patients')
        verbose_name = _('Patient')

    def __str__(self):
        return self.name
