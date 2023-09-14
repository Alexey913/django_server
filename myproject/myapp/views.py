from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Post, Comment
from .forms import RandForm, AuthorForm, PostForm, CommentForm
import logging
import datetime
from random import randint as rnd

logger = logging.getLogger(__name__)


def rand_form(request):
    if request.method == 'POST':
        form = RandForm(request.POST)
        if form.is_valid():
            kind = form.cleaned_data['kind']
            count_tries = form.cleaned_data['count_tries']
            logger.info(
                f'Ввод {kind} - {count_tries} - {datetime.datetime.now()}')
            return rand(request, kind=kind, count=count_tries)
    else:
        form = RandForm()
    return render(request, 'myapp/rand_form.html', {'form': form})


def rand(request, kind, count):
    side_coin = ['Орел', 'Решка']
    if kind == 'coin':
        res_kind = 'Монета'
        result = {i: side_coin[rnd(0, 1)] for i in range(1, count+1)}
        logger.info(f'Подброшена монета - {datetime.datetime.now()}')
    elif kind == 'cube':
        res_kind = 'Кубик'
        result = {i: [rnd(1, 6)] for i in range(1, count+1)}
        logger.info(f'Брошен кубик - {datetime.datetime.now()}')
    elif kind == 'number':
        res_kind = 'Случайное число'
        result = {i: f'=={rnd(1, 100)}==' for i in range(1, count+1)}
        logger.info(f'Случайное число - {datetime.datetime.now()}')
    context = {'title': res_kind, 'result': result}
    return render(request, 'myapp/rand_result.html', context)


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(name=form.cleaned_data['name'],
                            surname=form.cleaned_data['surname'],
                            email=form.cleaned_data['email'],
                            biography=form.cleaned_data['biography'],
                            birthday=form.cleaned_data['birthday'],
                            )
            author.save()
            logger.info(f'Создан автор {author} - {datetime.datetime.now()}')
            return render(request, 'myapp/sucsess.html', {'title': 'Запись добавлена', 'type': 'автор', 'content': author})
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_form.html', {'form': form, 'title': 'Добавить автора'})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'],
                        post_body=form.cleaned_data['post_body'],
                        date_publication=form.cleaned_data['date_publication'],
                        author=Author.objects.get(
                            pk=form.cleaned_data['author']),
                        category=form.cleaned_data['category'],
                        )
            post.save()
            logger.info(f'Созданана статья {post} - {datetime.datetime.now()}')
            return render(request, 'myapp/sucsess.html', {'title': 'Запись добавлена', 'type': 'статья', 'content': post})
    else:
        form = PostForm()
    return render(request, 'myapp/add_form.html', {'form': form, 'title': 'Добавить статью'})


def index(request):
    authors = Author.objects.all()
    return render(request, 'myapp/author_list.html', {'authors': authors})


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'myapp/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.count_view += 1
    post.save()
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=Author.objects.get(pk=form.cleaned_data['author']),
                              post = post,
                              comment = form.cleaned_data['comment'],
                              date_create = datetime.date.today(),
                              date_change = datetime.date.today(),
                              )
            comment.save()
            logger.info(f'Созданан комментарий {comment} к статье {comment.post} - {datetime.datetime.now()}')
            # return render(request, 'myapp/sucsess.html', {'title': 'Запись добавлена', 'type': 'комментарий', 'content': post})
    else:
        form = CommentForm()
        
    return render(request, 'myapp/post_full.html', {'post': post, 'comments': comments, 'form': form})
