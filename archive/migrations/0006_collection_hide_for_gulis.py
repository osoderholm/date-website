# Generated by Django 5.0.10 on 2024-12-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20221004_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='hide_for_gulis',
            field=models.BooleanField(default=False, verbose_name='Göm för gulisar'),
        ),
    ]
