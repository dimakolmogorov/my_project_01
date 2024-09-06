from django.core.management.base import BaseCommand
from my_app_2.models import Users


class Command(BaseCommand):
    help = 'Update user name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('email', type=str, help='Username')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = kwargs.get('email')
        user = Users.objects.filter(pk=pk).first()
        user.email = email
        user.save()
        self.stdout.write(f"{user}")