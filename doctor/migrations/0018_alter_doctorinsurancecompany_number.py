# Generated by Django 4.0.2 on 2022-02-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_doctorinsurancecompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinsurancecompany',
            name='number',
            field=models.CharField(max_length=255, null=True, verbose_name='Number'),
        ),
    ]
