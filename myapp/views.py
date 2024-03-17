from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
import logging
from django.views.generic import TemplateView

from .forms import UserForm, ImageForm, ProductForm, ProductModelForm
from .models import Order, User, Product

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page open")
    return render(request, 'main.html')


def about(request):
    logger.info("About page open")
    return render(request, 'about.html')


def my_view(request):
    context = {"name": "Alex"}
    return render(request, "myapp/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp/templ_for.html', context)


def view_orders(request, user_id):
    logger.info("Orders page open")
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-date_ordered')[:4]
    context = {'orders': orders, 'user': user}
    return render(request, 'orders.html', context)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            user = User(name=name, email=email, phone_number=phone_number, password=password,
                        address=address)
            user.save()
            logger.info(f"User {user.name} created")
            message = f'Пользователь {user.name} сохранен'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def product_form(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(name=name, price=price, description=description, count=count,
                              image=image)
            product.save()
            logger.info(f"Product {product.name} created")
            message = f'Продукт {product.name} сохранен'
    else:
        form = ProductModelForm()
        message = 'Заполните форму'
    return render(request, 'product_form.html', {'form': form, 'message': message})
