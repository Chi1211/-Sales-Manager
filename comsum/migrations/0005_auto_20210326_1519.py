# Generated by Django 2.2 on 2021-03-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comsum', '0004_statisticalmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statisticalmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='statisticalmodel',
            name='material_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
