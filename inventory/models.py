from django.db import models
from django.db.models.deletion import CASCADE
from django import utils

class Products(models.Model):
    itemid = models.AutoField(primary_key=True)
    manufacture = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    category = models.CharField(max_length=150,null=True,blank=True)
    serialnumber = models.IntegerField(null=True,blank=True)
    item = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    price = models.FloatField(blank=True,null=True)
    notes = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return '{} {} {}'.format(self.manufacture,self.item,self.serialnumber)

class Transactions(models.Model):
    transactiondate = models.DateField(default=utils.timezone.now)
    quantity = models.IntegerField(null=True,blank=True)
    itemid = models.ForeignKey(Products,default=119,on_delete=CASCADE)
    hh = models.IntegerField(null=True,blank=True)
    issuer = models.CharField(max_length=150,null=True,blank=True)
    checkoutdate = models.DateField(default=utils.timezone.now, null=True,blank=True)
    checkindate = models.DateField(default=utils.timezone.now, null=True,blank=True)
    notes = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return '{} {} {}'.format(self.transactiondate,self.itemid,self.issuer)