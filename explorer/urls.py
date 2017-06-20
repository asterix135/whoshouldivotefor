from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from explorer import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^playground/$', views.Playground.as_view(), name='playground'),

    # url(r'^api/$', views.api_root),
    # url(r'^polity/$', views.PolityList.as_view(), name="polity-list"),
    # url(r'^polity/(?P<pk>[0-9]+)/$', views.PolityDetail.as_view(),
    #     name='polity-detail'),
    # url(r'^users/$', views.UserList.as_view(), name="user-list"),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
    #     name='user-detail'),
    # url(r'^api_root/$', views.api_root),

    ################
    # REST login
    ################
    # url(r'^api-auth/', include('rest_framework.urls')),


]

urlpatterns = format_suffix_patterns(urlpatterns)
