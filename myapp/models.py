from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    phone_number = models.IntegerField(verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адресс')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    date_register = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f"Username - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    count = models.IntegerField(verbose_name='Количество')
    image = models.ImageField(blank=True, verbose_name='Вид продукта')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"Product - {self.name}, count: {self.count}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Итоговая цена')

    def __str__(self):
        return f"Order by {self.customer.name}, total: {self.total_price}. Date: {self.date_ordered}"
