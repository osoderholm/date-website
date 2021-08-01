# Generated by Django 3.0.14 on 2021-04-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_url', models.URLField(max_length=255)),
                ('company_url', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]
