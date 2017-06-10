from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from explorer import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    ################
    # REST urls
    ################
    url(r'^polity/$', views.PolityList.as_view()),
    url(r'^polity/(?P<pk>[0-9]+)/$', views.PolityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
