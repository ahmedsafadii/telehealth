from django.db import models
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):
    doctor = models.ForeignKey("doctor.Doctor", on_delete=models.DO_NOTHING, related_name="bookings",
                               blank=False, null=True, verbose_name=_("Doctor"))
    patient = models.ForeignKey("patient.Patient", on_delete=models.DO_NOTHING, related_name="bookings",
                                blank=False, null=True, verbose_name=_("Patient"))
    consultation_type = models.ForeignKey("setting.Consultation", on_delete=models.DO_NOTHING,
                                          null=True,
                                          related_name="bookings", verbose_name=_("Consultation type"))
    price = models.FloatField(blank=False, null=True, verbose_name=_("Price"))
    date = models.DateField(null=True, blank=False, verbose_name=_("Date"))
    time = models.ForeignKey("doctor.DoctorTimeSlot", on_delete=models.DO_NOTHING, related_name="time",
                             blank=False, null=True, verbose_name=_("Time"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Bookings')
        verbose_name = _('Booking')

    def __str__(self):
        return str(self.id)
