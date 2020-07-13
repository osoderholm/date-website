# Generated by Django 2.1.1 on 2018-09-13 13:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Namn')),
                ('does_expire', models.BooleanField(default=True, verbose_name='Upphör')),
                ('renewal_scale', models.CharField(choices=[('day', 'Dagar'), ('month', 'Månader'), ('year', 'År')], max_length=10, null=True, verbose_name='Förnyelse skala')),
                ('renewal_period', models.IntegerField(blank=True, null=True, verbose_name='Förnyelseperiod')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Pris')),
            ],
            options={
                'verbose_name': 'prenumeration',
                'verbose_name_plural': 'prenumerationer',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateField(default=django.utils.timezone.now, verbose_name='Betald')),
                ('date_expires', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Betald')),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Betald summa')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Subscription')),
            ],
            options={
                'verbose_name': 'prenumerationsbetalning',
                'verbose_name_plural': 'prenumerationsbetalningar',
                'ordering': ('id',),
            },
        ),
    ]
