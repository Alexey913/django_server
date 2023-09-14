from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = "Create client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client e-mail')
        parser.add_argument('phone', type=int, help='Client phone')
        parser.add_argument('adress', type=str, help='Client adress')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        adress = kwargs.get('adress')
        client = Client(name=name,
                        email=email,
                        phone=phone,
                        adress=adress,
                        )
        client.save()
        self.stdout.write(f'Создана запись {client}')
