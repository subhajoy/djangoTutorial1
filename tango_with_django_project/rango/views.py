from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)

def index1(request):
    return HttpResponse("Rango says lol Hey there partner!")

def about(request):
    return HttpResponse("Rango says this is about page!")