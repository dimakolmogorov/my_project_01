from django.core.management.base import BaseCommand
from my_app_2.models import Users


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        #user = Users(name='dima', email='dima.kolmogorov.93@mail.ru', password='secret', age=30)
        #user = Users(name='Neo', email='neo_matrix_93@mail.ru', password='secret', age=40)
        user = Users(name='Hacker', email='hacker93@mail.ru', password='secret', age=39)
        ...
        user.save()
        self.stdout.write(f'{user} created')