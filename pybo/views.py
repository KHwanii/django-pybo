from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>안녕 그지깽깽이들아</h1> Pybo에 온것을 환영한다.")
# Create your views here.
