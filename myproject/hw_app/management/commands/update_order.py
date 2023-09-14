from django.core.management.base import BaseCommand
from hw_app.models import Goods, Client, Order
from decimal import Decimal


class Command(BaseCommand):
    help = "Update order"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=str, help='Client_id')
        parser.add_argument('goodses', type=str, help='List of goods id')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        goodses = kwargs.get('goodses').split()
        order = Order.objects.filter(pk=order_id).first()
        for g in order.goods.all():
            order.goods.remove(g)
        common_price = 0
        for goods_id in goodses:
            goods = Goods.objects.filter(pk=goods_id).first()
            order.goods.add(goods)
            common_price += goods.price
        order.common_price = common_price
        order.save()

        self.stdout.write(f'Изменен заказ № {order.pk}')
