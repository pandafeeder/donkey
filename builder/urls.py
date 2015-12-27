# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import page 

urlpatterns = (
    url(r'^$', page, name='index'),
    url(r'^(?P<slug>[\w.\-_@\?]+)/$', page, name='page'),
)
