from  datetime import datetime
from django.shortcuts import render, HttpResponse
def hello(request):
    
    return HttpResponse("Hello")

