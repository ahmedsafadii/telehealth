# Generated by Django 4.0.2 on 2022-02-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='address_ar',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address_ro',
        ),
    ]