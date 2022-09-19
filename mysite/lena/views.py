from django.shortcuts import render

def lena(request):
    return render(request,"lena.html",{})
