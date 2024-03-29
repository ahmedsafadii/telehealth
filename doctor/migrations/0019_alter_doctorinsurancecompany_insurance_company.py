# Generated by Django 4.0.2 on 2022-02-09 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('doctor', '0018_alter_doctorinsurancecompany_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinsurancecompany',
            name='insurance_company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='setting.insurancecompany', verbose_name='Insurance company'),
        ),
    ]
