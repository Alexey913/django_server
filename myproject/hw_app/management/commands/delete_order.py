from django.core.management.base import BaseCommand
from hw_app.models import Goods, Client, Order


class Command(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            for g in order.goods.all():
                order.goods.remove(g)
            self.stdout.write(f'Удален заказ № {order.pk}')
            order.delete()