from django.core.management.base import BaseCommand
from my_app_2.models import Author, Post


class Command(BaseCommand):
    help = "Get post by author ID"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            intro = f'All posts of {author.name}\n'
            text = '\n'.join(post.content for post in posts)
            self.stdout.write(f"{intro}{text}")
