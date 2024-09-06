"""
URL configuration for my_project_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_my_3.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('my_app.urls')),
    path('app3/', include('app_my_3.urls')),
    path('', index),
    path('lesson4/', include('app4.urls')),
    #path('__debug__/', include('debug_toolbar.urls')),
    path('les6/', include('app6.urls'))
]


