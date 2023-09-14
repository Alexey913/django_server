from django.core.management.base import BaseCommand
from myapp.models import Post

class Command(BaseCommand):
    help = "Get all posts"
    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        self.stdout.write(f'{posts}')