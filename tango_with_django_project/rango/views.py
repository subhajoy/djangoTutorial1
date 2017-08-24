from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hey there partner! <br /> <a href='/rango/about/'>About</a>")

def index1(request):
    return HttpResponse("Rango says lol Hey there partner!")

def about(request):
    return HttpResponse("Rango says this is about page!")