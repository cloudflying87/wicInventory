from django import forms
from .models import Inventory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset,Field
# from dal import autocomplete

class InventoryEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Inventory Form',
                Row(
                    Column('transactiondate',type='date',css_class='form-group col-sm-3 mb-1'),
                    Column('issuer',css_class='form-group col-sm-3 mb-1'),
                    Column('hh',css_class='form-group col-sm-3 mb-1'),
                ),
                Row(
                    Column('item',css_class='form-group col-sm-3 mb-1'),
                    Column('quantity',css_class='form-group col-sm-3 mb-1'),
                    Column('checkoutdate',css_class='form-group col-sm-3 mb-1'),
                    Column('checkindate',css_class='form-group col-sm-3 mb-1'),
                    Column('notes',css_class='form-group col-sm-3 mb-1'),
                )
                
            ),
            Submit('Submit','save')
        )
    class Meta:
        model = Inventory
        fields = ('transactiondate','issuer','hh','item','quantity','checkoutdate','checkindate','notes')
        # widgets= {
        #     'item':autocomplete.ModelSelect2(url='autocomplete')
        # }