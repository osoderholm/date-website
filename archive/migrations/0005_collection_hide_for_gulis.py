# Generated by Django 3.1.13 on 2022-08-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_auto_20210713_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='hide_for_gulis',
            field=models.BooleanField(default=False, verbose_name='Göm för gulisar'),
        ),
    ]