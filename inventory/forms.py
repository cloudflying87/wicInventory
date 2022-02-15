from django import forms
from django.db.models.query import QuerySet
from .models import Transactions, Products
from django.forms import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset,Div

# from dal import autocomplete

def custom_form_fieldCallback(field, **kwargs):
    category_query = Products.objects.exclude(category = 'pump')
    
    if field.name == 'itemid':
        print(category_query)
        return category_query
    else:
        return field.formfield(**kwargs)

TransactionFormSet = modelformset_factory(
    Transactions, fields=('transactiondate','hh','itemid','quantity'),extra=1
)
class TransactionEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # self.name=kwargs.pop('intial')
        super(TransactionEntry,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['issuer'] = forms.CharField(initial=self.name)
        self.fields['transactiondate'].label = "Date"
        self.fields['hh'].label = "Household #"
        self.fields['itemid'].label = "Item Name"
        self.fields['itemid'].queryset = Products.objects.exclude(category = 'pump')
        self.fields['quantity'].label = "Quantity"
        self.helper.form_id = 'topform'
        self.helper.form_class = 'form-main'
        self.helper.layout = Layout(
            Fieldset(
                'Inventory Form',
                Div(
                    'transactiondate',
                    'hh',
                    'itemid',
                    'quantity',
                    css_id='topthree',
                ),            
            ),
            Submit('Submit','save')
        )
    class Meta:
        model = Transactions
        fields = ('transactiondate','hh','itemid','quantity','checkoutdate','checkindate')


class PumpEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # self.name=kwargs.pop('intial')
        super(PumpEntry,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['issuer'] = forms.CharField(initial=self.name)
        self.fields['transactiondate'].label = "Date"
        self.fields['hh'].label = "Household #"
        self.fields['itemid'].label = "Item Name"
        self.fields['quantity'].label = "Quantity"
        self.helper.form_id = 'topform'
        self.helper.form_class = 'form-main'
        self.helper.layout = Layout(
            Fieldset(
                'Inventory Form',
                Div(
                    'transactiondate',
                    'hh',
                    'itemid',
                    'quantity',
                    'notes',
                    css_id='topthree',
                ),            
            ),
            Submit('Submit','save')
        )
    class Meta:
        model = Transactions
        fields = ('transactiondate','issuer','hh','itemid','quantity','checkoutdate','checkindate','notes')
 
