from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','stock','image']

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise forms.ValidationError('El precio debe ser mayor a 0')
            return price
        def clean_stock(self):
            stock = self.cleaned_data.get('stock')
            if stock <= 0:
                raise forms.ValidationError('El stock debe de ser mayor a 0')
            return stock
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['name'].label = 'Nombre:'
            self.fields['description'].widget.attrs['class'] = 'form-control'
            self.fields['description'].label = 'Descripción:'
            self.fields['price'].widget.attrs['class'] = 'form-control'
            self.fields['price'].label = 'Precio ($):'
            self.fields['stock'].widget.attrs['class'] = 'form-control'
            self.fields['stock'].label = 'Stock:'
            self.fields['image'].widget.attrs['class'] = 'form-control'
            self.fields['image'].label = 'Foto:'
    #name = forms.CharField(label="Nombre:",widget=forms.TextInput(attrs={'class': 'form-control'}))
