from django.core.management.base import BaseCommand
from my_app_2.models import Users


class Command(BaseCommand):
    help = 'Get all users'

    def handle(self, *args, **kwargs):
        users = Users.objects.all()
        self.stdout.write(f'{users}')
        