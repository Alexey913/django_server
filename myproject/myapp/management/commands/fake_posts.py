from django.core.management.base import BaseCommand
from myapp.models import Author, Post
from random import randint as rnd
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create fake posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of posts')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        temp = 0
        for author in Author.objects.all():
            for i in range(1, count+1):
                post = Post(title=f'title_{i}',
                            post_body=f'{"very interesting post"*rnd(1, i+1)}',
                            date_publication=f'{date.today() - timedelta(days=rnd(1, i+1))}',
                            author=author,
                            category=f'category_{rnd(1,i+1)}',
                            count_view=rnd(0, i*100),
                            publication=rnd(0, 1),
                            )
                post.save()
                temp += 1
        self.stdout.write(f'Создано {temp} статей')
