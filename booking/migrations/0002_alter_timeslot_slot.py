# Generated by Django 4.0.2 on 2022-02-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='slot',
            field=models.TimeField(max_length=1, null=True, verbose_name='Time slot'),
        ),
    ]
