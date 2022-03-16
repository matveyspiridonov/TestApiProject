from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #print(HttpResponse("Hello, world. You're at the polls index.").content)
    return HttpResponse("Hello, world. You're at the polls index.")
