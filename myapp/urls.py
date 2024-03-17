from django.urls import path
from . import views
from .views import TemplIf, view_for, view_orders, user_form, upload_image, product_form

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('orders/<int:user_id>', view_orders, name='orders'),
    path('user/add/', user_form, name='user_form'),
    path('upload/', upload_image, name='upload_image'),
    path('product/add/', product_form, name='product_form'),
]
