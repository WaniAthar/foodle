# This file is made by the developer not by django---

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")