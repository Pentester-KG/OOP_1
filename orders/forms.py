from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSearchForm(forms.Form):
    order_id = forms.IntegerField(label="Номер заказа")
