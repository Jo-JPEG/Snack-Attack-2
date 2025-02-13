from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'snake/index.html')

def snake(request):
    return render(request, 'snake/snake.html')