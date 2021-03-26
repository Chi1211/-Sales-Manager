# Generated by Django 2.2 on 2021-03-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comsum', '0003_consumptionmodel_saveconsumption_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255)),
                ('material_digital', models.IntegerField()),
                ('material_reality', models.IntegerField()),
            ],
        ),
    ]
