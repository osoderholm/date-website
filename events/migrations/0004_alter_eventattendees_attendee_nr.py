# Generated by Django 4.1.7 on 2023-03-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20220820_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattendees',
            name='attendee_nr',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='#'),
        ),
    ]
