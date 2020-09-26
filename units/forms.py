from django import forms
from .models import Unit

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        #fields = '__all__'
        #fields = ['title','description','price']
        exclude = ['created_at',]