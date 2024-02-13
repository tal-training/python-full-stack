from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django")

def home(request):
    return HttpResponse("Hello again")
