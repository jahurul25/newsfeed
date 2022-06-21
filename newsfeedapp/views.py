from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests, random, string

# Create your views here.

User = get_user_model()

def user_login(request):
    try:
        if request.method == "GET":

            return render(request, 'login.html')
        elif request.method == "POST":
            user_email = request.POST.get('user_email').lower()
            user_pass  = request.POST.get('user_pass') 

            user = authenticate(request, username=user_email, password=user_pass)
            if user and user.is_staff==True:           
                login(request, user)
                return redirect("home") 
            else:
                return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def signup(request):
    try:
        if request.method == "GET":

            return render(request, 'signup.html')
        elif request.method == "POST":
            user_email = request.POST.get('user_email').lower()
            user_pass  = request.POST.get('user_pass') 
            first_name = request.POST.get('first_name') 
            last_name  = request.POST.get('last_name') 

            user = User.objects.create(username=user_email, email=user_email, first_name=first_name, last_name=last_name, is_active=True, is_staff=True)
            user.set_password(user_pass)
            user.save()

            return redirect("user_login")
    except:
        return render(request, 'signup.html')

def reset_password(request):
    if request.method == "POST":
        user_email  = request.POST.get('user_email')    

        user = User.objects.get(username=user_email)
        if user:  
            random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
            user.set_password(random_password)
            user.save()

            context = {
                "msg": "Password reset successfully. Please check your email"
            } 
        else:
            context = {
                "msg": "Your email doesn't match!"
            } 
        return render(request, 'reset_password.html', context)
    else:
        return render(request, 'reset_password.html')

@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return redirect("user_login") 

@login_required(login_url="user_login")
def home(request):

    return render(request, 'index.html')

@login_required(login_url="user_login")
def newsfeed_settings(request):

    return render(request, 'newsfeed_settings.html')