from django.shortcuts import render

# Create your views here.

def login(request):
    template = "main/login.html"
    return render(request, template)
