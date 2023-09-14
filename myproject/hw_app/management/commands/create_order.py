from django.core.management.base import BaseCommand
from hw_app.models import Goods, Client, Order
from decimal import Decimal


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=str, help='Client_id')
        parser.add_argument('goodses', type=str, help='List of goods id')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        goodses = kwargs.get('goodses').split()
        client = Client.objects.filter(pk=client_id).first()
        order = Order(client=client,
                      )
        order.save()
        common_price = 0
        for goods_id in goodses:
            goods = Goods.objects.filter(pk=goods_id).first()
            order.goods.add(goods)
            common_price += goods.price
            goods.quantity -= 1
            goods.save()
        order.common_price = common_price
        order.save()

        self.stdout.write(f'Создан {order}')