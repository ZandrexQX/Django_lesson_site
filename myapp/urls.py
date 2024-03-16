from django.urls import path
from . import views
from .views import TemplIf, view_for, view_orders

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('orders/<int:user_id>', view_orders, name='orders'),
]
