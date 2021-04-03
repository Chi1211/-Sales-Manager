# Generated by Django 2.2 on 2021-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comsum', '0006_consumpfoodmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('amount', models.IntegerField(primary_key=True, serialize=False)),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GetStatistics',
            fields=[
                ('month', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='consumpfoodmodel',
            name='price',
        ),
        migrations.AddField(
            model_name='consumpfoodmodel',
            name='food_price',
            field=models.IntegerField(default=1),
        ),
    ]