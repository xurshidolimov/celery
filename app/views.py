from django.shortcuts import render
from django.http import HttpResponse
from .tasks import slow


def index(request):
    slow.delay(123456789)
    return HttpResponse("Working!!!!!")
