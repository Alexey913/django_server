import datetime
from django import forms
from .models import Author

class RandForm(forms.Form):
    kind = forms.ChoiceField(label='Что бросаем?', choices=[('coin', 'Бросок монеты'), ('cube', 'Бросок кубика'), ('number', 'Случайное число')])
    count_tries = forms.IntegerField(label='Сколько раз?', min_value=1, max_value=64)

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    surname = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(label='E-mail')
    biography = forms.CharField(widget=forms.Textarea,
                                label='Биография')
    birthday = forms.DateField(initial=datetime.date.today(),
                               label='Дата рождения',
                               widget=forms.DateInput(attrs={'type': 'date'}))
    

class PostForm(forms.Form):
    title = forms.CharField(max_length=200,
                            label='Название статьи')
    post_body = forms.CharField(widget=forms.Textarea,
                                label='Текст статьи')
    date_publication = forms.DateField(initial=datetime.date.today(),
                                       label='Дата публикации',
                                       widget=forms.DateInput(attrs={'type': 'date'}))
    author = forms.ChoiceField(label='Автор', choices=[(author.pk, f'{author.name} {author.surname}') for author in Author.objects.all()])
    category = forms.CharField(label='Категория', max_length=100)

class CommentForm(forms.Form):
    author = forms.ChoiceField(label='Автор', choices=[(author.pk, f'{author.name} {author.surname}') for author in Author.objects.all()])
    comment = forms.CharField(widget=forms.Textarea,
                                label='Текст комментария')