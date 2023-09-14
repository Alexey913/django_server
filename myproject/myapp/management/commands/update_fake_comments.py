from django.core.management.base import BaseCommand
from myapp.models import Comment
from random import randint as rnd
from datetime import timedelta


class Command(BaseCommand):
    help = 'Update date fake comments'

    def handle(self, *args, **kwargs):
        temp = 0
        for comment in Comment.objects.all():
            comment.date_create = comment.date_create - timedelta(days=rnd(50, 150))
            comment.save()
            if comment.post.publication:
                comment.date_change = comment.date_create + timedelta(days=rnd(5, 15))
                comment.save()
            temp+=1
        self.stdout.write(f'Обновлено {temp} комментариев')