from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def java(request):
    return HttpResponse ('<h1> java core java </h1>')
