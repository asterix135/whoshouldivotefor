from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView

from rest_framework import generics, permissions, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import *
# from .permissions import IsOwnerOrReadOnly
# from .serializers import *

class Index(TemplateView):
    template_name = 'explorer/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['greeting'] = 'Hello! ' * 2
        return context

#
# class PolityList(generics.ListCreateAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PolityDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly)
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'polities': reverse('polity-list', request=request, format=format)
#     })
