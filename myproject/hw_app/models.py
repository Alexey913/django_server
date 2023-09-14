from django.db import models
from datetime import date
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=200, default=None)
    date_registration = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Goods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_adding = models.DateField(default=timezone.now)


    def __str__(self) -> str:
        return f'{self.title}'
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods)
    common_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    date_create = models.DateField(default=timezone.now)
   
    def __str__(self) -> str:
        return f'Заказ на сумму {self.common_price}'