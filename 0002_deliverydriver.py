# Generated by Django 5.0.1 on 2024-02-11 10:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryDriver',
            fields=[
                ('driverID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('driverName', models.CharField(max_length=50)),
                ('driverHp', models.CharField(max_length=11)),
                ('dApproveStatus', models.CharField(max_length=10)),
                ('vehicleDes', models.CharField(max_length=50)),
                ('currentOrders', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, null=True, size=None)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=11)),
            ],
        ),
    ]
