from django.urls import path
from .views import hello, HelloView, year_post, MonthPost, post_detail
from .views import index, about, my_view, TempIf, view_for

from .views import view_for
from .views import index, about
from .views import author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='template'),
    path('if/', TempIf.as_view(), name='template_if'),
    path('for/', view_for, name='template_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post_full/<int:post_id>/', post_full, name='post_full'),
]

