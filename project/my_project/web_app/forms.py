from django import forms
from .models import Marketplace

class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = ['title', 'description', 'photo', 'price', 'email']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название товара',
            'description': 'Описание',
            'photo': 'Фотография',
            'price': 'Цена (руб.)',
            'email': 'Email для связи',
        }