from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField


class Country(models.Model):
    name = TranslatedField(
        models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Name"))
    )

    code = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Code"))

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Countries')
        verbose_name = _('Country')

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                null=False, blank=False, verbose_name=_("Country"), related_name="cities")
    name = TranslatedField(
        models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Name"))
    )

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Cities')
        verbose_name = _('City')

    def __str__(self):
        return self.name
