from django.core.management.base import BaseCommand
from hw_app.models import Order


class Command(BaseCommand):
    help = "Read order by id"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=str, help='Order id')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        order = Order.objects.filter(pk=order_id).first()
        self.stdout.write(f'Заказ № {order.pk}:\n')
        for num, goods in enumerate(order.goods.all(), start=1):
            self.stdout.write(f'{num}. {goods.title} - {goods.price} руб.')
        self.stdout.write(f'Итоговая стоимость - {order.common_price} руб.')
