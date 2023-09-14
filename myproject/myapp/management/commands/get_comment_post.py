from django.core.management.base import BaseCommand
from myapp.models import Comment, Author, Post


class Command(BaseCommand):
    help = "Get comments to post"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Post title')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        post = Post.objects.filter(title=title).first()
        if post is not None:
            comments = Comment.objects.filter(post=post)
            intro = f'Все комментарии к статье {post.title}\n'
            text = '\n'.join(comment.comment for comment in comments)
            self.stdout.write(f'{intro}{text}')
        else:
            self.stdout.write('Комментариев не найдено')