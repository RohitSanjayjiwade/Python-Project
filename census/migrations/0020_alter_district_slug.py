# Generated by Django 4.2.8 on 2023-12-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0019_alter_district_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
