from django import forms
from django.db.models.query import QuerySet
from .models import Transactions, Products, Category, Manufacture
from django.forms import modelformset_factory
from django.forms.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset,Div
from dal import autocomplete

TransactionFormSet = modelformset_factory(
    Transactions, fields=('transactiondate','hh','itemid','quantity'),extra=1
)

InventoryUpdate = modelformset_factory(
    Products, fields=('quantitydate','manufacture','item','price','quantity'),extra=1
)

class InventoryDrop(forms.ModelForm):
    manufacture = forms.ModelChoiceField(queryset=Manufacture.objects.all(),initial=8)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),initial=12)
    class Meta:
        model = Products
        fields = ('manufacture','category')
        

class HHTest(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('hh',)

class TransactionEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransactionEntry,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['transactiondate'].label = "Date"
        self.fields['hh'].label = "Household #"
        self.fields['itemid'].label = "Item Name"
        # self.fields['itemid'].queryset = Products.objects.exclude(category = 10)
        self.fields['quantity'].label = "Quantity"
        self.helper.form_id = 'topform'
        self.helper.form_class = 'form-main'
        self.helper.layout = Layout(
            Fieldset(
                'Inventory Form',
                Div(
                    Div(
                        'transactiondate',
                        'hh',
                        'itemid',
                        'quantity',
                        css_id='topthree',
                    ), 
                    css_id = 'parentdiv'
                ),
                Submit('Submit', 'Save')           
            ),
        )
    class Meta:
        model = Transactions
        fields = ('transactiondate','hh','itemid','quantity')
    
        widgets = {
            'itemid': autocomplete.ModelSelect2(url='itemlookup'),
            'transactiondate': DateInput(attrs={'type': 'date'}),

        }

class PumpCheckin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # self.name=kwargs.pop('intial')
        super(PumpCheckin,self).__init__(*args, **kwargs)
        self.fields['itemid'].label = "Pump"
        self.fields['itemid'].queryset = Products.objects.filter(category = 10, quantity = 0  )
        self.fields['transactiondate'].label = "Date"
    class Meta:
        model = Transactions
        fields = ('itemid','notes','transactiondate')
        widgets = {
            'transactiondate': DateInput(attrs={'type': 'date'}),
        }

class PumpStatus(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # self.name=kwargs.pop('intial')
        super(PumpStatus,self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        self.fields['hh'].label = "Household #"
        self.fields['itemid'].label = "Pump"
        self.fields['checkoutdate'].label = "Check-out Date"
        self.fields['checkindate'].label = "Check-in Date"
        self.fields['itemid'].queryset = Products.objects.filter(category = 10, quantity = 0  )
    class Meta:
        model = Transactions
        fields = ('itemid','hh','notes','checkoutdate','checkindate')
        widgets = {
            'checkoutdate': DateInput(attrs={'type': 'date'}),
            'checkindate': DateInput(attrs={'type': 'date'}),
        }
class PumpEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PumpEntry,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['transactiondate'].label = "Date"
        self.fields['hh'].label = "Household #"
        self.fields['itemid'].label = "Pump"
        self.fields['checkoutdate'].label = "Check-out Date"
        self.fields['checkindate'].label = "Check-in Date"
        self.fields['itemid'].queryset = Products.objects.filter(category = 10, quantity = 1  )
        self.helper.form_id = 'topform'
        self.helper.form_class = 'form-main'
        self.helper.layout = Layout(
            Fieldset(
                'Pump Checkout',
                Div(
                    'transactiondate',
                    'hh',
                    'itemid',
                    'notes',
                    css_id='topthree',
                ),            
            ),
            
        )
    class Meta:
        model = Transactions
        fields = ('itemid','hh','notes','transactiondate','checkoutdate','checkindate')
        widgets = {
            'transactiondate': DateInput(attrs={'type': 'date'}),
            'checkoutdate': DateInput(attrs={'type': 'date'}),
            'checkindate': DateInput(attrs={'type': 'date'}),
        }
 
