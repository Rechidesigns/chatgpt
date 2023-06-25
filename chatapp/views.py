from django.shortcuts import render

# Create your views here.


def index (request):
    context = {}
    return render(request, "chatapp/index.html", context)


def signup (request):
    context = {}
    return render(request, "chatapp/signup.html", context)


def signin (request):
    context = {}
    return render(request, "chatapp/signin.html", context)
