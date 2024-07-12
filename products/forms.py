from django import forms
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
    
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 4:
            raise forms.ValidationError("This is not long enough")
        return data
