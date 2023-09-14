from django.contrib import admin
from .models import Client, Goods, Order
from datetime import datetime


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_registration']
    ordering = ['name', '-date_registration']
    list_filter = ['name', 'date_registration']
    search_fields = ['adress']
    search_help_text = 'Поиск по адресу (adress)'
    fields = ['name', 'phone', 'adress']
    readonly_fields = ['name']


@admin.action(description="Обнулить количество товара")
def update_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']
    ordering = ['-price', 'title', 'quantity']
    list_filter = ['price', 'title', 'quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию товара (description)'
    fields = ['title', 'description', 'price', 'quantity', 'date_adding']
    readonly_fields = ['title', 'date_adding']
    actions = [update_quantity]

@admin.action(description="Изменить дату заказа на сегодняшнюю")
def change_date(modeladmin, request, queryset):
    queryset.update(date_create=datetime.today())

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'common_price', 'id', 'date_create']
    ordering = ['id', '-common_price', '-date_create']
    list_filter = ['client', 'date_create']
    search_fields = ['id']
    search_help_text = 'Поиск по номеру заказа'
    # fields = ['id', 'client', 'common_price', 'goods']
    actions = [change_date]
    readonly_fields = ['id']
    fieldsets = [
        (
            'Заказ №',
            {
                'classes': ['wide'],
                'fields': ['id'],
                # 'readonly_fields': ['id'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Дата заказа и стоимость',
                'fields': ['date_create', 'common_price'],
            },
        ),
        (
            'Состав заказа',
            {
                'description': 'Перечень товаров, входящее в заказ',
                'fields': ['goods'],
            }
        ),
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
