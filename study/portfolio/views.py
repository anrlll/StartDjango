from django.shortcuts import render

#HttpResponse import
from django.http import HttpResponse

def helloworldfunc1(request):
    return HttpResponse('hello portfolio')
