from datetime import datetime
from django.shortcuts import render, HttpResponse


def solve(request):
    a = 0
    b = 0
    result = 0
    cmd = ""
    if request.GET:

        a = request.GET["a"]
        b = request.GET["b"]
        cmd = request.GET["cmd"]
        if cmd == "Add":
            result = int(a)+int(b)
        if cmd == "Sub":
            result = int(a)-int(b)

    # return HttpResponse("Hi")
    return render(request, "solve.html", {"a": a, "b": b, "result": result})


def hello(request):

    return HttpResponse("Hello")


def arithmeticstart(request):

    # return HttpResponse("Hi")
    return render(request, "arithmetic.html", {1: "Dhoni"})


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
