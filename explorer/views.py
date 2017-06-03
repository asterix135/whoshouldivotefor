from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Home Page for WhoShouldIVoteFor.ca</h2>')
