# Generated by Django 4.2.8 on 2023-12-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0015_city_city_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='village_code',
            field=models.CharField(default='', max_length=30),
        ),
    ]