# Generated by Django 2.2 on 2021-03-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0008_auto_20210323_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getimportmaterialmodel',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='importmaterialmodel',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=19),
        ),
    ]
