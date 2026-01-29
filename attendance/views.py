from  datetime import datetime
from django.shortcuts import render, HttpResponse
def hello(request):
    
    return HttpResponse("Hello")
def hi(request):
    
    # return HttpResponse("Hi")
    return render(request,"hi.html")


