import datetime
from django import forms
from .models import Goods, Order

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(min_length=2, max_length=100, label='Телефон')
    adress = forms.CharField(max_length=200, label='Адрес')

class GoodsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Наименование')
    description = forms.CharField(label='Описание', widget=forms.Textarea())
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')
    quantity = forms.IntegerField(min_value=1, label='Количество')


class OrderForm(forms.Form):
    goods = forms.ChoiceField(label='Добавить товар', choices=[(goods.pk, f'{goods.title} {goods.price}') for goods in Goods.objects.all()])

class ImageForm(forms.Form):
    image = forms.ImageField(label='Добавить фото')