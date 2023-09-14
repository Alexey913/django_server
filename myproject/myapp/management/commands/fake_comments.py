from django.core.management.base import BaseCommand
from myapp.models import Author, Post, Comment
from random import randint as rnd
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create fake comments'

    def handle(self, *args, **kwargs):
        temp = 0
        for post in Post.objects.all():
            for author in Author.objects.all():
                comment = Comment(author=author,
                                  post=post,
                                  comment=f'Комментарий автора {author} к статье {post}',
                                  date_create=f'{date.today() - timedelta(days=rnd(5, 10))}',
                                  date_change=f'{date.today() - timedelta(days=rnd(1, 3))}',
                                  )
                comment.save()
                temp += 1
        self.stdout.write(f'Создано {temp} комментариев')
