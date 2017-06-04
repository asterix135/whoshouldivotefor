from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    # return HttpResponse('<h2>Home Page for WhoShouldIVoteFor.ca</h2>')
    return render(request, 'explorer/index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'explorer/db.html', {'greetings': greetings})
