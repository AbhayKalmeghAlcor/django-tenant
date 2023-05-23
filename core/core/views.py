from django.http import request
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello this is multi-tenant application")
