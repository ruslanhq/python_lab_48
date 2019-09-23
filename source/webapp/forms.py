from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Category')
    count = forms.IntegerField(min_value=0, required=True, label='Amount')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Price', required=True)


# class SearchForm(forms.Form):
#     form = forms.CharField(max_length=40, label='Form', required=False)
