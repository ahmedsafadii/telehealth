# Generated by Django 4.0.2 on 2022-02-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('doctor', '0011_alter_doctorconsultation_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='specialities',
            field=models.ManyToManyField(to='setting.Speciality', verbose_name='Specialities'),
        ),
    ]
