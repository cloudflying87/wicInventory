from nis import cat
from tokenize import Number
from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from .models import Transactions,Products
from .forms import HHTest, PumpEntry, InventoryDrop, TransactionEntry,TransactionFormSet,InventoryUpdate,PumpCheckin, PumpStatus
from django.db.models import Count, Sum
import datetime
from django.urls import reverse_lazy
from dal import autocomplete

# class InventoryAutoComplete(autocomplete.Select2QuerySetView):
    
#     def get_queryset(self):
        
#         qs = Products.objects.all()
        
#         print(self)
#         if self.q:
#             qs = qs.filter(item__istartswith=self.q)
#         return qs

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transaction_add')
        else:
            messages.success(request, "Incorrect username or password.")
            return redirect('/')

    else:
        return render(request, 'inventory/signin.html', {})

@login_required(login_url='/add')
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
            return redirect(reverse_lazy("report"))

        return self.render_to_response({'transaction_formset': formset})

class PumpCheckin(FormView):
    template_name = 'inventory/pumpcheckin.html'
    
    form_class = PumpCheckin


    success_url ="pumpcheckin"

    def form_valid(self, form):

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
         
        # perform a action here
        
        form.save()
        item = Products.objects.get(itemid=form.data['itemid'])
        item.quantity = 1
        item.save()
        return super().form_valid(form)
class PumpCheckout(FormView):
    template_name = 'inventory/pumpcheckout.html'
    
    form_class = PumpEntry


    success_url ="pumpcheckout"

    def form_valid(self, form):
        form.save()
        item = Products.objects.get(itemid=form.data['itemid'])
        item.quantity = 0
        item.save()
        return super().form_valid(form)

class PumpStatus(FormView):
    template_name = 'inventory/pumpstatus.html'
    
    form_class = PumpStatus


    success_url ="pumpstatus"

    def form_valid(self, form):
        print(form.data)
        form.save()
        return super().form_valid(form)

def get_manufacture(request):
    manufacture = request.GET.get('manufacture')
    category = request.GET.get('category')
    if manufacture == None:
        inventory = Products.objects.filter(category=category).order_by('item')    
    if category == None:
        inventory = Products.objects.filter(manufacture=manufacture).order_by('item')
    
    if category != None and manufacture != None:
        inventory = Products.objects.filter(manufacture=manufacture,category=category).order_by('item')

    if category == None and manufacture == None: 
        inventory = Products.objects.all().order_by('item')
    
    
    return render(request,'inventory/manufacture.html',{'inventory':inventory}) 

def transactions(request):
    hh = request.GET.get('hh')
    information = Transactions.objects.filter(hh=hh).order_by('transactiondate')
    print(information)
    return render(request,'inventory/manufacture.html',{'inventory':information}) 

def pumpstatus(request):
    itemid = request.GET.get('itemid')
    information = Transactions.objects.filter(itemid=itemid).order_by('transactiondate')
    hh1 = Transactions.objects.filter(itemid=itemid).last()
    
    # if hh1 != None:
    if hh1.hh == None:
        hh = 1234
    else:
        hh = hh1.hh
    
    if hh1.checkoutdate == None:
        checkoutdate = ''
    else:
        checkoutdate = (hh1.checkoutdate).strftime("%Y-%d-%d")
    return render(request,'inventory/pumpnotesdisplay.html',{'pumpnotes':information,'hh':hh,'checkoutdate':checkoutdate}) 
class TransactionsView(TemplateView):
    template_name = 'inventory/report.html'
    def get(self, *args, **kwargs):
        pagetitle = "Report"
        formset = formset_factory(HHTest)
        return self.render_to_response({'transaction_formset':formset,"title":pagetitle})
class InventoryDropView(TemplateView):
    template_name = 'inventory/inventorydrop.html'
    def get(self, *args, **kwargs):
        pagetitle = "Inventory Report"
        formset = formset_factory(InventoryDrop)
        return self.render_to_response({'transaction_formset':formset,"title":pagetitle})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return redirect('/')
