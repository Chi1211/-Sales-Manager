# Generated by Django 2.2 on 2021-03-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_materialmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialmodel',
            name='material_amount',
        ),
        migrations.RemoveField(
            model_name='materialmodel',
            name='unit_name',
        ),
    ]
