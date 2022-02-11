# Generated by Django 4.0.2 on 2022-02-09 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_alter_doctorinsurancecompany_insurance_company'),
        ('booking', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='doctor.doctor', verbose_name='Doctor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.timeslot', verbose_name='Doctor'),
        ),
    ]