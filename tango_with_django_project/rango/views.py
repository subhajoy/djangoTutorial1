from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake'}
    return render(request, 'rango/index.html', context=context_dict)

def index1(request):
    return HttpResponse("Rango says lol Hey there partner!")

def about(request):
    return HttpResponse("Rango says this is about page!")