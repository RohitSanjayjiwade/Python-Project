# Generated by Django 4.2.8 on 2023-12-08 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0009_alter_data_area_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='rural_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_rural_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='city',
            name='urban_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_urban_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='data',
            name='district_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='data',
            name='state_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='data',
            name='sub_district_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='data',
            name='town_village_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='district',
            name='rural_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_rural_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='district',
            name='urban_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_urban_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='state',
            name='rural_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_rural_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='state',
            name='urban_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_urban_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='village',
            name='rural_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_rural_data', to='census.data'),
        ),
        migrations.AddField(
            model_name='village',
            name='urban_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_urban_data', to='census.data'),
        ),
        migrations.AlterField(
            model_name='city',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_data', to='census.data'),
        ),
        migrations.AlterField(
            model_name='data',
            name='area_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='enumeration_block_code',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='level_of_admin_unit',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='total_rural_urban',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='ward_code',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='district',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_data', to='census.data'),
        ),
        migrations.AlterField(
            model_name='state',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_data', to='census.data'),
        ),
        migrations.AlterField(
            model_name='village',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_data', to='census.data'),
        ),
    ]
