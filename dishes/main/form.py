from django import forms
from .models import Contact




class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name',  'email', 'address',  'note', 'adv', 'telephone' , 'id' )


       


        widgets = {'first_name': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'שם' , 'rows': 1, 'dir':"rtl"}), 
        
         'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מייל' , 'rows': 1, 'dir':"rtl"}),

         'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'טלפון' , 'rows': 1, 'dir':"rtl"}),
        
           'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'כתובת' , 'rows': 1, 'dir':"rtl"}), 
            
               'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'הודעה' , 'rows': 4, 'dir':"rtl"}),
               
                  'transport': forms.RadioSelect()}