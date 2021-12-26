from django import forms
from .models import Transactions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset,Div

# from dal import autocomplete

class TransactionEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # self.name=kwargs.pop('intial')
        super(TransactionEntry,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['issuer'] = forms.CharField(initial=self.name)
        self.fields['transactiondate'].label = "Date"
        self.fields['issuer'].label = "Issuer"
        self.helper.form_id = 'topform'
        self.helper.form_class = 'form-main'
        self.helper.layout = Layout(
            Fieldset(
                'Inventory Form',
                Div(
                    'transactiondate',
                    'issuer',
                    'hh',
                    css_id="topthree"
                ),
                Div(
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
        # widgets= {
        #     'item':autocomplete.ModelSelect2(url='autocomplete')
        # }