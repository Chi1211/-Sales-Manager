# Generated by Django 2.2 on 2021-03-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comsum', '0005_auto_20210326_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumpFoodModel',
            fields=[
                ('food_id', models.IntegerField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, max_digits=19)),
            ],
        ),
    ]
