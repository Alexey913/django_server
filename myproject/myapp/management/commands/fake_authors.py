from django.core.management.base import BaseCommand
from myapp.models import Author
from random import randint as rnd
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create fake authors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of authors')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count+1):
            author = Author(name=f'name_{i}',
                            surname=f'surname_{i}{i}',
                            email=f'mail{i}@super.ru',
                            biography=f'{"bla_bla_bla_"*rnd(1, i+1)}',
                            birthday=f'{date.today() - timedelta(days=rnd(1, i+1))}',
            )
            author.save()
        self.stdout.write(f'Создано {count} авторов')