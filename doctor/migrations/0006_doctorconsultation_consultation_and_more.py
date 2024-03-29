# Generated by Django 4.0.2 on 2022-02-09 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('doctor', '0005_doctorconsultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorconsultation',
            name='consultation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='setting.consultation', unique=True, verbose_name='Doctor'),
        ),
        migrations.AlterField(
            model_name='doctorconsultation',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='doctor.doctor', verbose_name='Doctor'),
        ),
        migrations.AlterUniqueTogether(
            name='doctorconsultation',
            unique_together={('doctor', 'consultation')},
        ),
    ]
