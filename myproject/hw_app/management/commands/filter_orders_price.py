from django.core.management.base import BaseCommand
from hw_app.models import Goods, Client, Order
from decimal import Decimal


class Command(BaseCommand):
    help = "Update order"

    def add_arguments(self, parser):
        parser.add_argument('condition', type=str, help='Condition of filters')
        parser.add_argument('price', type=Decimal, help='Price to filter')

    def handle(self, *args, **kwargs):
        condition = kwargs['condition']
        price = kwargs.get('price')
        if condition == 'more':
            orders = Order.objects.filter(common_price__gte=price)
        elif condition == 'less':
            orders = Order.objects.filter(common_price__lte=price)
        elif condition == 'equals':
            orders = Order.objects.filter(common_price=price)
        if orders:
            for order in orders:
                self.stdout.write(f'Заказ № {order.pk} - {order.common_price} руб.')
        else:
            self.stdout.write(f'Заказов не найдено')