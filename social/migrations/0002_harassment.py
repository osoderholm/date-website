# Generated by Django 4.2.6 on 2023-10-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harassment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('message', models.TextField(max_length=1500, verbose_name='Beskrivning av händelsen')),
            ],
        ),
    ]