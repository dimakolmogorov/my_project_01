from django.core.management.base import BaseCommand
from my_app_2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'my_mail{i}@mail.ru')
            author.save()
            for j in range(count + 1):
                post = Post(
                    title = f'Title{j}',
                    content = f'This is text from {author.name} with title{j} bla bla bla',
                    author=author
                )
                post.save()