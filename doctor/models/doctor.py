from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor",
                                blank=False, null=False, verbose_name=_("User"))

    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    gender = models.CharField(max_length=1, null=True, blank=False, choices=GENDER_CHOICES, verbose_name=_("Gender"))

    picture = models.ImageField(upload_to="doctors/profile_pictures", blank=True, null=True, verbose_name=_("Picture"))

    country = models.ForeignKey("setting.Country", on_delete=models.CASCADE, related_name="doctors",
                                blank=False, null=True, verbose_name=_("Country"))

    city = models.ForeignKey("setting.City", on_delete=models.CASCADE, related_name="doctors",
                             blank=False, null=True, verbose_name=_("City"))

    phone = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Phone"))

    address = models.TextField(blank=False, null=True, verbose_name=_("Address"))

    bio = models.TextField(blank=False, null=True, verbose_name=_("Bio"))

    specialities = models.ManyToManyField("setting.Speciality", blank=False, verbose_name=_("Specialities"),
                                          related_name="specialities")

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name_plural = _('Doctors')
        verbose_name = _('Doctor')

    def __str__(self):
        return self.user.username


class DoctorConsultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultations",
                               blank=False, null=True, verbose_name=_("Doctor"))
    consultation = models.OneToOneField("setting.Consultation", on_delete=models.CASCADE,
                                        related_name="doctors",
                                        blank=False, null=True, verbose_name=_("Consultation"))
    price = models.FloatField(null=True, blank=False, verbose_name=_("Price"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        unique_together = ('doctor', 'consultation')
        verbose_name_plural = _('Doctor Consultations')
        verbose_name = _('Doctor Consultation')

    def __str__(self):
        return self.doctor.user.username


class DoctorInsuranceCompany(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="insurance_companies",
                               blank=False, null=True, verbose_name=_("Doctor"))
    insurance_company = models.OneToOneField("setting.InsuranceCompany", on_delete=models.CASCADE,
                                             related_name="doctors",
                                             blank=False, null=True, verbose_name=_("Insurance company"))
    number = models.CharField(max_length=255, null=True, blank=False, verbose_name=_("Number"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        unique_together = ('doctor', 'insurance_company')
        verbose_name_plural = _('Doctor Insurance companies')
        verbose_name = _('Doctor Insurance Company')

    def __str__(self):
        return self.doctor.user.username


class DoctorTimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="slots",
                               blank=False, null=True, verbose_name=_("Doctor"))
    start_time = models.TimeField(max_length=1, null=True, blank=False, verbose_name=_("Start time"))
    end_time = models.TimeField(max_length=1, null=True, blank=False, verbose_name=_("End time"))
    is_free = models.BooleanField(default=True, blank=False, null=True, verbose_name=_("Is free"))
    note = models.CharField(max_length=255, blank=False, null=True, verbose_name=_("Note"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        unique_together = ('start_time', 'end_time')
        verbose_name_plural = _('Doctor time slots')
        verbose_name = _('Doctor time slot')

    def __str__(self):
        return str(self.start_time) + " " + str(self.end_time)
