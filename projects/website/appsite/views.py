from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ambi(request):
    return HttpResponse("<h1>Hello Ambi</h1>")
