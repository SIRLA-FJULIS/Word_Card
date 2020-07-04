"""word_card URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from word_set.views import home, cards, set_new, set_edit, set_delete, word_status, register
# from account.views import register
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    re_path(r'^set/(?P<pk>\d+)/$', cards, name="cards"),
    re_path(r'^set/new/$', set_new, name='set_new'),
    re_path(r'^set/(?P<pk>[0-9]+)/edit/$', set_edit, name='set_edit'),
    re_path(r'^set/(?P<pk>[0-9]+)/delete/$', set_delete, name='set_delete'),
    re_path(r'^word/(?P<pk>[0-9]+)/update/$', word_status, name='word_status'),
]
