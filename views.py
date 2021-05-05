from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ologin(request):
    return render(request,"ologin.html")
