# Generated by Django 4.0.2 on 2022-02-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0024_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doctortimeslot',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='doctortimeslot',
            name='end_time',
            field=models.TimeField(max_length=1, null=True, verbose_name='End time'),
        ),
        migrations.AddField(
            model_name='doctortimeslot',
            name='start_time',
            field=models.TimeField(max_length=1, null=True, verbose_name='Start time'),
        ),
        migrations.AlterUniqueTogether(
            name='doctortimeslot',
            unique_together={('start_time', 'end_time')},
        ),
        migrations.RemoveField(
            model_name='doctortimeslot',
            name='slot',
        ),
    ]