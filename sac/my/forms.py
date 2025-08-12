from django import forms
from .models import product

class Pform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'price', 'description']  # use your actual field names
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }