import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *

class Index(TemplateView):
    template_name = 'explorer/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['greeting'] = 'Hello! ' * 2
        return context
