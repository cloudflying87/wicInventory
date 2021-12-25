from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from dal import autocomplete
from .models import Inventory
from .forms import InventoryEntry

# class InventoryAutComplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = Inventory.objects.all()
        
#         if self.q:
#             qs = qs.filter(icao__istartswith=self.q)
#         return qs

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkout')
        else:
            messages.success(request, "Incorrect username or password.")
            return redirect('/')

    else:
        return render(request, 'inventory/signin.html', {})

# @login_required(login_url='/')
def checkout(request):
    print(request)
    pagetitle="WIC Entry"
    if request.method == "POST":
        inventoryform = InventoryEntry(request.POST)
        if inventoryform.is_valid():
            inventoryform.save()
    inventoryform = InventoryEntry()
    return render(request, 'inventory/checkout.html', {'pagetitle':pagetitle, 'inventoryform':inventoryform})

def report(request):
    hello = "Report"
    pagetitle= "Report"
    return render(request, 'inventory/report.html', {'pagetitle':pagetitle,'hello':hello})

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return redirect('/')
