# Generated by Django 4.2.6 on 2023-11-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_captcha'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistrationform',
            name='choice_number',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='#'),
        ),
    ]
