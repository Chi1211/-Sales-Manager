# Generated by Django 2.2 on 2021-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210327_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailbillmodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
