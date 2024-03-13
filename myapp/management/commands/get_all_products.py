from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **options):
        products = Product.objects.all()
        self.stdout.write(f'{products}')