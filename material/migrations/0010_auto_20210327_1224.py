# Generated by Django 2.2 on 2021-03-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0009_auto_20210324_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getimportmaterialmodel',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=19),
        ),
        migrations.AlterField(
            model_name='importmaterialmodel',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=19),
        ),
    ]
