# Generated by Django 4.0.2 on 2022-02-11 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_insurancecompany_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_companies', to='setting.country', verbose_name='Country'),
        ),
    ]
