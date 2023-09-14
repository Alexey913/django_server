from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Client, Goods, Order
from .forms import ClientForm, GoodsForm, ImageForm, OrderForm
from datetime import date, timedelta, datetime
from random import randint as rnd
import logging

logger = logging.getLogger(__name__)


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    context = {'client': client, 'orders': orders}
    return render(request, 'hw_app/client_orders.html', context)


def orders_term(request, client_id, term):
    client = get_object_or_404(Client, pk=client_id)
    filter_date = date.today() - timedelta(days=term)
    orders = Order.objects.filter(
        client=client, date_create__gte=filter_date).order_by('-date_create')
    goodses = {}
    for order in orders:
        for goods in order.goods.all():
            goodses[goods] = order.date_create
    goodses = dict(sorted(goodses.items(), key=lambda kv: kv[1], reverse=True))
    context = {'client': client, 'goodses': goodses, 'term': term}
    return render(request, 'hw_app/orders_term.html', context)


def goods_description(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hw_app/goods_description.html', {'goods': goods, 'form': form})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client(name=form.cleaned_data['name'],
                            email=form.cleaned_data['email'],
                            phone=form.cleaned_data['phone'],
                            adress=form.cleaned_data['adress'],
                            )
            client.save()
            logger.info(f'Создан клиент {client} - {datetime.now()}')
            return render(request, 'hw_app/sucsess.html', {'title': 'Запись добавлена', 'type': 'клиент', 'content': client})
    else:
        form = ClientForm()
    return render(request, 'hw_app/add_form.html', {'form': form, 'title': 'Добавить клиента'})


def create_goods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            goods = Goods(title=form.cleaned_data['title'],
                          description=form.cleaned_data['description'],
                          price=form.cleaned_data['price'],
                          quantity=form.cleaned_data['quantity'],
                          )
            goods.save()
            logger.info(f'Создан клиент {goods} - {datetime.now()}')
            return render(request, 'hw_app/sucsess.html', {'title': 'Запись добавлена', 'type': 'товар', 'content': goods})
    else:
        form = GoodsForm()
    return render(request, 'hw_app/add_form.html', {'form': form, 'title': 'Добавить товар'})


def change_order(request, client_id, order_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            goods = Goods.objects.filter(pk=form.cleaned_data['goods']).first()
            client = Client.objects.get(pk=client_id)
            if order_id == 0:
                order = Order(client=client, common_price=goods.price)
                order.save()
                order.goods.add(goods)
                order.save()
                logger.info(f'Изменен заказ {order} - {datetime.now()}')
            else:
                order = Order.objects.filter(pk=order_id).first()
                for g in order.goods.all():
                    if goods == g:
                        return render(request, 'hw_app/sucsess.html', {'title': f'{goods} уже есть в заказе', 'type': '----', 'content': order, 'back': client})
                order.goods.add(goods)
                order.common_price += goods.price
                goods.quantity -= 1
                order.save()
                logger.info(f'Изменен заказ {order} - {datetime.now()}')
            return render(request, 'hw_app/sucsess.html', {'title': 'Запись добавлена', 'type': 'заказ', 'content': order, 'back': client})
    else:
        form = OrderForm()
    return render(request, 'hw_app/add_form.html', {'form': form, 'title': 'Редактировать заказ'})


def index(request):
    clients = Client.objects.all()
    return render(request, 'hw_app/client_list.html', {'clients': clients})
