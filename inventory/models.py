from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save
from django.db.models.deletion import CASCADE
from django import utils
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django_currentuser.middleware import (
    get_current_user)

def add_time():
    #used to add 3 months to the pump checkout date
    today = datetime.now()
    future_date = today + relativedelta(months = 3)
    return future_date
class Products(models.Model):
    itemid = models.AutoField(primary_key=True)
    manufacture = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    category = models.CharField(max_length=150,null=True,blank=True)
    serialnumber = models.IntegerField(null=True,blank=True)
    item = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    quantity = models.IntegerField()
    quantitydate = models.DateField(default=utils.timezone.now)
    price = models.FloatField(blank=True,null=True)
    notes = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        if self.serialnumber == 0:
            serialnumberrep = ''
        else:
            serialnumberrep = self.serialnumber
        return '{} {} {} {}'.format(self.manufacture,self.item,serialnumberrep,self.quantity)

class Transactions(models.Model):
    transactiondate = models.DateField(default=utils.timezone.now)
    quantity = models.IntegerField(null=True,blank=True)
    itemid = models.ForeignKey(Products,default=119,on_delete=CASCADE)
    hh = models.IntegerField(null=True,blank=True)
    issuer = models.CharField(max_length=150,null=True,blank=True)
    checkoutdate = models.DateField(default=utils.timezone.now, null=True,blank=True)
    checkindate = models.DateField(default=add_time, null=True,blank=True)
    notes = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return '{} {} {}'.format(self.transactiondate,self.itemid,self.issuer)



def pre_save_transactions(sender,instance,*args,**kwargs):
    currentuser = str(get_current_user())
    instance.issuer = currentuser
    
    item = Products.objects.get(itemid=instance.itemid_id)
    
    if instance.quantity != None:
        updatequantity = item.quantity - instance.quantity
        instance.quantity = -instance.quantity
        item.quantity = updatequantity
        item.save()
    else:
        instance.quantity = 0
    
    

pre_save.connect(pre_save_transactions, sender=Transactions)