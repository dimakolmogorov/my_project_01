from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Author, Post


def hello(request):
    return HttpResponse('Hello from function')


class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello from CLASS")


def year_post(request, year):
    text = ''
    ...
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = 'Вы открыли тестовую страницу, я учусь работать на джанго, привет из пайчарма'
        ...
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')


def post_detail(request, year, month, slug):
    ...
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': "Кто быстрее создает списки в пайтон? list()или []",
        'content': "В процессе написания программы задумался над тем, "
                   "какой способ создания списков в Python работает быстрее ..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': "Dimasik"}
    return render(request, 'app_my_3/template.html', context)


class TempIf(TemplateView):
    template_name = 'app_my_3/template_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Привет, друзья!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': "красный",
        "охотник": "оранжевый",
        "желает": "жёлтый",
        "знать": "зеленый",
        "где": "голубой",
        "сидит": "синий",
        "фазан": "фиолетовый"
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'app_my_3/template_for.html', context)


def index(request):
    return render(request, 'app_my_3/index.html')


def about(request):
    return render(request, 'app_my_3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'app_my_3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'app_my_3/post_full.html', {'post': post})