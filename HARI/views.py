from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def india(request):
    return HttpResponse ('<h1> HARI IS A STUDENT <h1>')

def python(request):
    return HttpResponse ('<h1> HELLO WORLD </h1>')
