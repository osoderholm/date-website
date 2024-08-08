# Generated by Django 5.0.3 on 2024-04-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0005_staticpage_nav_to_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticpage',
            name='category',
        ),
        migrations.RemoveField(
            model_name='staticpage',
            name='dropdown_element',
        ),
        migrations.AlterField(
            model_name='staticurl',
            name='dropdown_element',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='#'),
        ),
    ]