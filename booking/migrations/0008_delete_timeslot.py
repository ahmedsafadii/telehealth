# Generated by Django 4.0.2 on 2022-02-09 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0025_alter_doctortimeslot_unique_together_and_more'),
        ('booking', '0007_remove_booking_time_booking_end_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
