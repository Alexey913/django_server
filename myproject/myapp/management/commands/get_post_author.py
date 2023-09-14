from django.core.management.base import BaseCommand
from myapp.models import Post, Author


class Command(BaseCommand):
    help = "Get post by author."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Post Author name')
        parser.add_argument('surname', type=str, help='Post Author surname')

    def handle(self, *args, **kwargs):
        surname = kwargs.get('surname')
        name = kwargs.get('name')
        author = Author.objects.filter(name=name, surname=surname).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            intro = f'Все статьи от имени {author.name} {author.surname}\n'
            text = '\n'.join(post.title for post in posts)
            self.stdout.write(f'{intro}{text}')
        else:
            self.stdout.write('Статей не найдено')
