# Generated by Django 5.0.3 on 2024-03-26 22:52

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_event_redirect_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Innehåll'),
        ),
    ]