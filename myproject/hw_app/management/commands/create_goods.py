from datetime import date
from django.core.management.base import BaseCommand
from hw_app.models import Goods
from decimal import Decimal


class Command(BaseCommand):
    help = "Create goods"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Goods title')
        parser.add_argument('description', type=str, help='Goods description')
        parser.add_argument('price', type=Decimal, help='Goods price')
        parser.add_argument('quantity', type=int, help='Goods quantity')
        parser.add_argument('-d', type=str, help='date_adding', default=date.today())


    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        if isinstance(kwargs.get('d'), str):
            year, mounth, day = kwargs.get('d').split('-')
            date_adding = date(year=int(year), month=int(mounth), day=int(day))
        else:
            date_adding = kwargs.get('d')
        goods = Goods(title=title,
                      description=description,
                      price=price,
                      quantity=quantity,
                      date_adding=date_adding,
                      )
        goods.save()
        self.stdout.write(f'Создана запись {goods}')
