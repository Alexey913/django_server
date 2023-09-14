from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/<int:term>', views.orders_term, name='orders_term'),
    path('goods/<int:goods_id>/', views.goods_description, name='goods_description'),
    path('client/add', views.create_client, name='create_client'),
    path('goods/add', views.create_goods, name='create_goods'),
    path('', views.index, name='all_clients'),
    path('order/<int:client_id>/<int:order_id>', views.change_order, name='change_order'),
]