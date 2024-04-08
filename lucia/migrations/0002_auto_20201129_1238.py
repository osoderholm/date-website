# Generated by Django 3.0.3 on 2020-11-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lucia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='poll_url',
            field=models.URLField(default='', max_length=255, verbose_name='Poll URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='img_url',
            field=models.URLField(blank=True, max_length=255, verbose_name='Bild URL'),
        ),
    ]