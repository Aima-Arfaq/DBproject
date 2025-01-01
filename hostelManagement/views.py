from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("This is home page")
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    return HttpResponse("This is contact page")
