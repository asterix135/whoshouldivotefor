from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from api import views


# create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'polities', views.PolityViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router
# Additionally, include the login URLs for browsable API

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
