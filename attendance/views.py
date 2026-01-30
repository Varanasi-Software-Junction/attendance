from datetime import datetime
from django.shortcuts import render, HttpResponse


def hello(request):

    return HttpResponse("Hello")


def arithmeticstart(request):

    # return HttpResponse("Hi")
    return render(request, "arithmetic.html")


def calculate(request):
    a = int(request.GET["a"])
    b = int(request.GET["b"])
    cmd = request.GET["cmd"]
    result = ""
    if cmd == "Add":
        result = a+b
    elif cmd == "Sub":
        result = a-b
    print(a, b, cmd, result)

    return HttpResponse("Calculate")
    # return render(request,"arithmetic.html")
