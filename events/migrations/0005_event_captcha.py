# Generated by Django 4.2.7 on 2023-11-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_eventattendees_attendee_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='captcha',
            field=models.BooleanField(default=False, verbose_name='Captcha'),
        ),
    ]
