# Generated by Django 4.0.2 on 2022-02-11 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0028_alter_doctorotp_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='address_ar',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='bio_ar',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address_ro',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='bio_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='bio_ro',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name_ro',
        ),
    ]
