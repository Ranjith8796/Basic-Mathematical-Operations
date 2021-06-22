from django.shortcuts import render
# from django.http import request

def home(request):
    return render(request,'add/addd.html')

def adding(request):
    if request.method=='POST':
        a1=int(request.POST["num1"])
        a2=int(request.POST["num2"])
        a3=a1+a2
        return render(request,'add/result.html',{'result':a3})

def subtracting(request):
    if request.method=='POST':
        a1=int(request.POST["num1"])
        a2=int(request.POST["num2"])
        a3=a1-a2
        return render(request,'add/result.html',{'result':a3})

def multiplication(request):
    if request.method=='POST':
        a1=int(request.POST["num1"])
        a2=int(request.POST["num2"])
        a3=a1*a2
        return render(request,'add/result.html',{'result':a3})

def division(request):
    if request.method=='POST':
        a1=int(request.POST["num1"])
        a2=int(request.POST["num2"])
        a3=a1/a2
        return render(request,'add/result.html',{'result':a3})