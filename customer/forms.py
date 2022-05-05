
from cProfile import label
from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['mail','phone']

class NameForm(forms.ModelForm):
    
    class Meta:
        model = Fullname
        fields = ["FirstName","LastName","customerID"]
        