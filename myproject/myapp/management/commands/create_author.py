from django.core.management.base import BaseCommand
from myapp.models import Author
from random import randint as rnd
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Create author"
    def handle(self, *args, **kwargs):
        author = Author(name=f'Алексей',
                        surname=f'Шевцов',
                        email=f'al913@mail.ru',
                        biography=f'Все об авторе. Интересно до ужаса',
                        birthday=f'1990-09-24',
                        )
        author.save()
        self.stdout.write(f'Создана запись {author}')