from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Успешно')

def ind(request):
    return HttpResponse('Усп')


# Create your views here.
