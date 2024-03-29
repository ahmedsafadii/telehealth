# Generated by Django 4.0.2 on 2022-02-09 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('doctor', '0003_rename_address_ar_doctor_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='address',
            new_name='address_ar',
        ),
        migrations.AddField(
            model_name='doctor',
            name='address_en',
            field=models.TextField(null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='address_ro',
            field=models.TextField(null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='setting.city', verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='setting.country', verbose_name='Country'),
            preserve_default=False,
        ),
    ]
