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

# API Call:  http://127.0.0.1:8000/api/polities/1.json

class Index(TemplateView):
    template_name = 'explorer/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['greeting'] = 'Hello! ' * 2
        return context


class Playground(TemplateView):
    template_name = 'explorer/playground.html'
