from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a la operacion de sumas, restas y multiplicaciones de 2 numeros por medio de URL.")

def suma(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    var3 = var1 + var2
    result = "Resultado: %s + %s = %s" % (var1,var2,var3)
    return HttpResponse(result)

def resta(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    var3 = var1 - var2
    result = "Resultado: %s - %s = %s" % (var1,var2,var3)
    return HttpResponse(result)

def multiplicacion(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    var3 = var1 * var2
    result = "Resultado: %s x %s = %s" % (var1,var2,var3)
    return HttpResponse(result)