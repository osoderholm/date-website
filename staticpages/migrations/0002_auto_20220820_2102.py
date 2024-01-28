# Generated by Django 3.1.13 on 2022-08-20 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='dropdown_element',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='staticpage',
            name='members_only',
            field=models.BooleanField(default=False, verbose_name='Kräv inloggning'),
        ),
        migrations.AddField(
            model_name='staticpagenav',
            name='nav_element',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staticpages.staticpagenav'),
        ),
        migrations.CreateModel(
            name='StaticUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titel')),
                ('url', models.CharField(max_length=200, verbose_name='Url')),
                ('dropdown_element', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staticpages.staticpagenav')),
            ],
        ),
    ]