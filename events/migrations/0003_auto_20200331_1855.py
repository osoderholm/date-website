# Generated by Django 3.0.3 on 2020-03-31 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200116_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistrationform',
            name='published',
        ),
        migrations.AlterField(
            model_name='event',
            name='sign_up_cancelling_deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Avanmälningen stängs'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sign_up_deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Anmälningen stängs'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug'),
        ),
    ]