from django.shortcuts import render 

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

from django.shortcuts import HttpResponse, redirect
def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number {number}")

def destroy(request, number):
    return redirect('/')
