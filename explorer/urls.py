from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from explorer import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^polity/$', views.PolityList.as_view()),
    url(r'^polity/(?P<pk>[0-9]+)/$', views.PolityDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    ################
    # REST login
    ################
    url(r'^api-auth/', include('rest_framework.urls')),


]

urlpatterns = format_suffix_patterns(urlpatterns)
