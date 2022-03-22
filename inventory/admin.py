from django.contrib import admin
from .models import Products, Transactions, Category, Manufacture

admin.site.register(Products)
admin.site.register(Transactions)
admin.site.register(Category)
admin.site.register(Manufacture)