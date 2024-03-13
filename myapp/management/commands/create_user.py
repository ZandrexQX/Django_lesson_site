from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **options):
        user = User(name="Alex", email="Alex@mail.ru", phone_number=89001231231, password='secret', address="Krasnodar")
        ...
        user.save()
        self.stdout.write(f'{user}')