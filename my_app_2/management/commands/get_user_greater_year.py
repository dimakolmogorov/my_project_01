from django.core.management.base import BaseCommand
from my_app_2.models import Users


class Command(BaseCommand):
    help = 'Get user to year'

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help="User age")

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = Users.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
