# Generated by Django 4.0.2 on 2022-02-11 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_alter_insurancecompany_country'),
        ('doctor', '0027_doctorotp'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doctorotp',
            unique_together={('country', 'phone')},
        ),
    ]
