# Generated by Django 5.1.1 on 2024-11-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_event_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sign_up_max_participants',
            field=models.IntegerField(default=0, verbose_name='Maximal antal deltagare (0 för ingen begränsning)'),
        ),
    ]
