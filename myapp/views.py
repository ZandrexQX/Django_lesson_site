from django.shortcuts import render, get_object_or_404
import logging
from django.views.generic import TemplateView
from .models import Order, User

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
