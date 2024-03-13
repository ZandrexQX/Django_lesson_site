from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **options):
        product = Product(name="Product_1", price=1000, description="description of product", count=10)
        ...
        product.save()
        self.stdout.write(f'{product}')