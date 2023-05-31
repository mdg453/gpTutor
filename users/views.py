from django.shortcuts import render

# Create your views here.

def users(request):
    template = "main/users.html"
    return render(request, template)
