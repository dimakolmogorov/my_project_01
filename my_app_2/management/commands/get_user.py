from django.core.management.base import BaseCommand
from my_app_2.models import Users


class Command(BaseCommand):
    help = 'Get 1 user'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User_ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = Users.objects.filter(pk=pk).first()
        self.stdout.write(f"{user}")