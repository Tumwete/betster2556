# Generated by Django 4.0.5 on 2022-06-27 08:22

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0002_alter_bettingtip_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='bettingtip',
            name='country',
            field=django_countries.fields.CountryField(default='England', max_length=2),
        ),
    ]