from django.core.management.base import BaseCommand
from myapp.models import Post


class Command(BaseCommand):
    help = "Get post by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        post = Post.objects.filter(pk=pk).first()
        self.stdout.write(f'{post}')
