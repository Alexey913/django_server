from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.rand_form, name='rand_form'),
    path('random/<str:kind>/<int:count>/', views.rand, name='rand'),
    path('create_author/', views.create_author, name='authors_form'),
    path('create_post/', views.create_post, name='post_form'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
    path('index', views.index, name='main')
]