from django import forms
from .models import Order



TITLE_CHOICES = [
    ('y', 'y.'),
    ('u', 'u'),
    
]

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
       # transport = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES)),
        fields = ['first_name', 'last_name', 'email', 'telephone','address',  'city',  'note', 'company_name' ]
        
        widgets = {'first_name': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'שם' , 'rows': 1, 'dir':"rtl"}),
         'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'שם משפחה' , 'rows': 1, 'dir':"rtl"}),
         'company_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'פרטי\עסקי' , 'rows': 1, 'dir':"rtl"}),
         'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מייל' , 'rows': 1, 'dir':"rtl"}), 
         'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'טלפון' , 'rows': 1, 'dir':"rtl"}),
          'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'כתובת' , 'rows': 1, 'dir':"rtl"}), 
         
          'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'עיר' , 'rows': 1, 'dir':"rtl"}),
           'note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'הודעה' , 'rows': 4, 'dir':"rtl"}),
        }
           
           