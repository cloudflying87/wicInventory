from django.db import models
from django.db.models.signals import pre_save
from django_currentuser.middleware import (
    get_current_user)
from django.db.models.deletion import CASCADE
from django import utils
from datetime import datetime
from dateutil.relativedelta import relativedelta


def add_time():
    #used to add 3 months to the pump checkout date
    today = datetime.now()
    future_date = today + relativedelta(months = 3)
    return future_date
class Manufacture(models.Model):
    manufactureid = models.AutoField(primary_key=True)
    manufacture = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    manufacturenotes = models.CharField(max_length=350,null=True,blank=True) 

    class Meta:
        verbose_name_plural = "Manufacture"

    def __str__(self):
        return self.manufacture

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    categorynotes = models.CharField(max_length=350,null=True,blank=True) 
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

class Status(models.Model):
    statusid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    statusnotes = models.CharField(max_length=350,null=True,blank=True) 

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status
class Products(models.Model):
    itemid = models.AutoField(primary_key=True)
    manufacture = models.ForeignKey(Manufacture,on_delete=CASCADE)
    category = models.ForeignKey(Category, default="Generic",on_delete=CASCADE)
    serialnumber = models.IntegerField(null=True,blank=True)
    item = models.CharField(max_length=150,default = "Not Set",null=False,blank=False)
    quantity = models.IntegerField()
    quantitydate = models.DateField(default=utils.timezone.now)
    price = models.FloatField(blank=True,null=True)
    notes = models.CharField(max_length=500,null=True,blank=True)
    statusid = models.ForeignKey(Status,on_delete=CASCADE,default = 1)


    class Meta:
        verbose_name_plural = "Products"

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
    checkoutdate = models.DateField(null=True,blank=True)
    checkindate = models.DateField(null=True,blank=True)
    notes = models.CharField(max_length=500,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Transactions"
        
    def __str__(self):
        return '{} {} {} {} {}'.format(self.transactiondate,self.quantity,self.itemid.item,self.issuer,self.notes)



def pre_save_transactions(sender,instance,*args,**kwargs):
    currentuser = str(get_current_user())
    instance.issuer = currentuser
    item = Products.objects.get(itemid=instance.itemid_id)
    

    if instance.quantity != None:
        
        updatequantity = item.quantity - instance.quantity
        # instance.quantity = -instance.quantity
        item.quantity = updatequantity
        item.save()    
    

pre_save.connect(pre_save_transactions, sender=Transactions)