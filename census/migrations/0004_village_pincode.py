# Generated by Django 4.2.7 on 2023-12-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0003_alter_state_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='pincode',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]
