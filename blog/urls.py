"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .views import (
    index_view,
    post_list,
    post_create,
    post_detail,
    post_delete,
    post_update,
)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^list/', post_list, name='list'),
    url(r'^create/', post_create, name='create'),
    # d+ means that it will only accept digits
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', post_update, name='update'),
    url(r'^delete/', post_delete, name='delete'),
]
