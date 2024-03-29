# Generated by Django 5.0.1 on 2024-02-11 10:45

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_deliverydriver'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='DeliveryDriver',
            fields=[
                ('driverID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('driverName', models.CharField(max_length=50)),
                ('driverHp', models.CharField(max_length=15)),
                ('dApproveStatus', models.CharField(max_length=10)),
                ('vehicleDes', models.CharField(max_length=50)),
                ('currentOrders', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, null=True, size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_driver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
