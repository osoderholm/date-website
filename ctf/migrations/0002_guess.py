# Generated by Django 5.0.1 on 2024-02-06 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=200, verbose_name='Gissning')),
                ('correct', models.BooleanField(default=False, verbose_name='Korrekt')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Tid')),
                ('ctf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.ctf', verbose_name='CTF')),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.flag', verbose_name='Flagga')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Användare')),
            ],
            options={
                'verbose_name': 'Gissning',
                'verbose_name_plural': 'Gissningar',
            },
        ),
    ]