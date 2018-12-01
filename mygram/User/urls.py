from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^search/$', views.search_users),
    url(r'^user/(?P<user_id>\w+)/$', views.user, name='user'),
    path('', views.base, name="page"),
]