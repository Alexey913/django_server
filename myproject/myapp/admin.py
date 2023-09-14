from django.contrib import admin
from .models import Author, Post, Comment
from datetime import datetime

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'birthday']
    ordering = ['surname', 'birthday']
    list_filter = ['name', 'surname']
    fields = ['name', 'surname', 'birthday', 'email', 'biography']
    readonly_fields = ['name', 'surname', 'birthday']

@admin.action(description="Обновить дату публикации")
def update_date_publication(modeladmin, request, queryset):
    queryset.update(date_publication=datetime.today())

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_publication', 'category', 'count_view', 'author', 'publication']
    ordering = ['title', '-count_view', '-date_publication']
    list_filter = ['title', 'date_publication', 'category', 'author', 'publication']
    search_fields = ['post_body']
    search_help_text = 'Поиск по полю Содержимое статьи (post_body)'
    actions = [update_date_publication]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'date_create', 'date_change']
    ordering = ['post', '-date_create', '-date_change']
    list_filter = ['author', 'post', 'date_change']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

