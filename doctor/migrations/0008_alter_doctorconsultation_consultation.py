# Generated by Django 4.0.2 on 2022-02-09 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('doctor', '0007_alter_doctorconsultation_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorconsultation',
            name='consultation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='setting.consultation', verbose_name='Doctor'),
        ),
    ]