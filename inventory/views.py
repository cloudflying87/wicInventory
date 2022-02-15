from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.base import TemplateView
# from dal import autocomplete
from .models import Transactions,Products
from .forms import PumpEntry, TransactionEntry,TransactionFormSet,InventoryUpdate
from django.db.models import Count, Sum
import datetime
from django.urls import reverse_lazy

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
            return redirect('add')
        else:
            messages.success(request, "Incorrect username or password.")
            return redirect('/')

    else:
        return render(request, 'inventory/signin.html', {})

@login_required(login_url='/')
#This is the original attempt and looks pretty with the form formatted correctly, but you can only do one item at a time
def checkout(request):
    pagetitle="WIC Entry"
    data = request.user.username
    print(data)
    if request.method == "POST":
        transactionform = TransactionEntry(request.POST)
        if transactionform.is_valid():
            transactionform.save()
    else:
        
        transactionform = TransactionEntry()
    return render(request, 'inventory/checkout.html', {'title':pagetitle, 'transactionform':transactionform})

class InventorylistView(ListView):
    model = Products
    template_name = 'inventory/inventory.html'

class UpdateInventory(TemplateView):
    template_name = 'inventory/updateinventory.html'
    
    def get(self, *args, **kwargs):
        pagetitle = "Bulk Update Inventory"
        formset = InventoryUpdate()
        # formset = formset_factory(TransactionEntry)
        return self.render_to_response({'transaction_formset':formset,"title":pagetitle})
    
    def post(self, *args, **kwargs):
        
        formset = InventoryUpdate(data=self.request.POST)
        postdata = self.request.POST
        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("inventory_list"))

        return self.render_to_response({'transaction_formset': formset})
class TransactionAddView(TemplateView):
    template_name = 'inventory/addtransaction.html'
    
    def get(self, *args, **kwargs):
        pagetitle = "Inventory List"
        #formset = TransactionFormSet(queryset=Transactions.objects.none())
        formset = formset_factory(TransactionEntry)
        return self.render_to_response({'transaction_formset':formset,"title":pagetitle})
    
    def post(self, *args, **kwargs):
        
        formset = TransactionFormSet(data=self.request.POST)
        postdata = self.request.POST
        # Check if submitted forms are valid
        if formset.is_valid():
            numofforms = postdata['form-TOTAL_FORMS']
            print(numofforms)
            for eachform in numofforms:
                print(eachform)
                print('form-'+eachform+'-itemid')
            formset.save()
            return redirect(reverse_lazy("inventory_list"))

        return self.render_to_response({'transaction_formset': formset})

class PumpCheckout(TemplateView):
    template_name = 'inventory/pumpcheckout.html'
    
    def get(self, *args, **kwargs):
        pagetitle = "Pump Checkout"
        
        formset = formset_factory(PumpEntry)
        return self.render_to_response({'transaction_formset':formset,"title":pagetitle})
    
    def post(self, *args, **kwargs):
        
        formset = self.request.POST

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("inventory_list"))

        return self.render_to_response({'transaction_formset': formset})

def reportform(request):

    if request.method == "POST":
        item_searched = request.POST['item_searched']
    
        
        #Handles the blank form entry
        if item_searched == '':
            messages.success(request,"You forgot to type in an item")
            return render(request, 'inventory/report.html', {})
        
        
        print(item_searched)

def report(request):
    gettransactions = Products.objects.filter(category='pump')
    quantity = gettransactions[:5]
    # b = Products(itemid = 1, manufacture = 'Medela', category = 'pump', serialnumber = 0, item = 'Harmony Manual Pump', quantity = 10, quantitydate = '2021-12-26')
    b = Products.objects.all().get(itemid=1)
    b.quantity = 20
    b.save()
    # hello = "Report"
    pagetitle= "Report"
    return render(request, 'inventory/report.html', {'title':pagetitle,'quantity':quantity})

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return redirect('/')
