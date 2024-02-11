"""
Definition of models.
"""

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

#sharing entity

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

class DeliveryDriver(models.Model):
    driverID = models.CharField(primary_key=True, max_length=5)
    driverName = models.CharField(max_length=50)
    driverHp = models.CharField(max_length=11)
    dApproveStatus = models.CharField(max_length=10)
    vehicleDes = models.CharField(max_length=50)
    currentOrders = ArrayField(models.CharField(max_length=5), null=True, blank=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.driverID