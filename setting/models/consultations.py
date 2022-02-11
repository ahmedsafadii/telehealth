from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField


class Consultation(models.Model):
    name = TranslatedField(
        models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Name"))
    )

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Consultations')
        verbose_name = _('Consultation')

    def __str__(self):
        return self.name
