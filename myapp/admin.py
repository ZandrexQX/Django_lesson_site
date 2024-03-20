from django.contrib import admin
from .models import User, Product, Order


@admin.action(description='Сбросить в ноль')
def reset_count(modeladmin, request, queryset):
    queryset.update(count=0)

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']

    readonly_fields = ['date_register']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    ordering = ['name', '-price']
    list_filter = ['date_add', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю "Наименование"'
    actions = [reset_count]

    fields = ['date_add', 'name', 'description', 'price', 'count', 'image']
    readonly_fields = ['date_add']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']

    readonly_fields = ['date_ordered']
