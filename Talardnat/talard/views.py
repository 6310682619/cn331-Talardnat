from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'talard/index.html')

def about(request):
    return render(request, 'talard/about.html')

def allshop(request):
    return render(request, 'talard/allshop.html')