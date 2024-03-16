from django.core.management.base import BaseCommand
from myapp.models import Product, User, Order


class Command(BaseCommand):
    help = "Fill bd fake data."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count fake data')

    def handle(self, *args, **options):
        count = options.get('count')
        # for i in range(1, count + 1):
        #     product = Product(name=f"Product_{i}", price=1000,
        #                       description=f"description of product_{i}", count=10 * i)
        #     product.save()
        #     user = User(name=f"Name_{i}", email=f"Mail_{i}@mail.ru", phone_number=89001231231 + i,
        #                 password=f"secret_{i}", address="Krasnodar")
        #     user.save()

        for i in range(1, count + 1):
            user = User.objects.filter(pk=i).first()
            if user is not None:
                for j in range(1, count + 1):
                    product = Product.objects.filter(pk=j).first()
                    if product is not None:
                        order = Order(customer=user,
                                      total_price=product.price * i)
                        order.save()
                        order.products.set([product])
                        order.save()
