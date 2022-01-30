from django import forms
from django.forms.widgets import HiddenInput
from django.forms import NumberInput
from django.utils.translation import gettext_lazy as _

val = [(i,str(i)) for i in range(1, 101)]
                                                                                                
class Add_to_form(forms.Form):
    quantility = forms.IntegerField(min_value=-10, widget=NumberInput(attrs={'class': 'form-control',  'value': 1 }))
    update = forms.BooleanField(required= False, initial=False, widget=HiddenInput)

class Cart_add_remove(forms.Form):
    quantility = forms.IntegerField(min_value=1, widget=NumberInput(attrs={'class': 'form-control',  'value': 1 }))
    update = forms.BooleanField(required= False, initial=False, widget=HiddenInput)





