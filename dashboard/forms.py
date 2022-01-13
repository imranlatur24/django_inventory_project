from django.db import models
from django.forms import fields
from .models import ProductModel,Order
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields=['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']

