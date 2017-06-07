from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    # url(r'^db$', views.db, name='db'),
]
