from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField


class InsuranceCompany(models.Model):
    country = models.ForeignKey("setting.Country", on_delete=models.CASCADE,
                                null=True, blank=False, verbose_name=_("Country"), related_name="insurance_companies")

    name = TranslatedField(
        models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Name"))
    )

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Insurance companies')
        verbose_name = _('Insurance company')

    def __str__(self):
        return self.name
