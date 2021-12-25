from django.db import models
from django.db.models.deletion import CASCADE
import datetime
from django import utils

class Products(models.Model):
    manufacture = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    category = models.CharField(max_length=150,null=True,blank=True)
    serialnumber = models.IntegerField(null=True,blank=True)
    item = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    price = models.FloatField(blank=True,null=True)
    notes = models.CharField(max_length=500,null=True,blank=True)

class Inventory(models.Model):
    transactiondate = models.DateField(default=utils.timezone.now)
    quantity = models.IntegerField(null=True,blank=True)
    item = models.ForeignKey(Products,default='Not Set',on_delete=CASCADE)
    hh = models.IntegerField(null=True,blank=True)
    issuer = models.CharField(max_length=150,null=True,blank=True)
    checkoutdate = models.DateField(default=utils.timezone.now)
    checkindate = models.DateField(default=utils.timezone.now)
    notes = models.CharField(max_length=500,null=True,blank=True)