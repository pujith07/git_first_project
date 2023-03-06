from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def message(request):
    return HttpResponse('hai how are you')
def replay(request):
    return HttpResponse('im fine ')
