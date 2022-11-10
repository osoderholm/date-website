# Generated by Django 3.0.3 on 2020-03-31 15:55

import archive.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20200109_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCollection',
            fields=[
            ],
            options={
                'verbose_name': 'Dokumentarkiv',
                'verbose_name_plural': 'Dokumentarkiv',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('archive.collection',),
        ),
        migrations.CreateModel(
            name='PictureCollection',
            fields=[
            ],
            options={
                'verbose_name': 'Bildarkiv',
                'verbose_name_plural': 'Bildarkiv',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('archive.collection',),
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'dokument', 'verbose_name_plural': 'dokument'},
        ),
        migrations.AlterField(
            model_name='document',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Collection', verbose_name='Samling'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=archive.models.upload_to, verbose_name='Filnamn'),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Namn'),
        ),
    ]
