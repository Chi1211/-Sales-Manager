# Generated by Django 2.2 on 2021-03-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comsum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='getLossModel',
            fields=[
                ('material_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loss', models.IntegerField()),
            ],
        ),
    ]