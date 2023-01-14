from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Start screen")

# Create your views here.
