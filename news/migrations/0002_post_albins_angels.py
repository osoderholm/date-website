# Generated by Django 3.1.12 on 2021-08-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='albins_angels',
            field=models.BooleanField(default=False, verbose_name='Albins Angels'),
        ),
    ]
