from django.shortcuts import render
import requests

# Create your views here.

def login(request):
    try:
        if request.method == "GET":

            return render(request, 'login.html')
        elif request.method == "POST":
            user_name = request.POST.get('user_name')
            user_pass = request.POST.get('user_pass')

            return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def home(request):

    return render(request, 'login.html')