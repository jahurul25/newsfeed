from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests, json, random, string
from newsfeedapp.sendgridemail import SendGridEmailSend
from newsfeedapp import models
from django.core.cache import cache
from django.contrib import messages
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

        try:
            user = User.objects.get(username=user_email)
            if user:  
                random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
                user.set_password(random_password)
                user.save()
                SendGridEmailSend.sendEmail(user_email, subject="Did you change your password!", html_content="<h1> Your current password is: {} </h1>".format(str(random_password)))
                messages.success(request, "Password reset successfully. Please check your email" )
                return redirect("user_login")
            else:
                messages.warning(request, "Password reset failed. Email doesn't match!" ) 
                return render(request, 'reset_password.html')
        except:
            messages.warning(request, "Password reset failed. Email doesn't match!" )
            return render(request, 'reset_password.html') 
    else:
        return render(request, 'reset_password.html')

@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return redirect("user_login") 

@login_required(login_url="user_login")
def home(request):
    user_settings = models.NewsfeedSettings.objects.filter(user_id = request.user.id, deleted=False)
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=880be7984e8546d1a4e4f00471040890"
    response = requests.get(url)
    data = response.json()

    context = {
        "news_data": data["articles"]
    }
    return render(request, 'index.html', context)

@login_required(login_url="user_login")
def newsfeed_settings(request):
    if request.method == "GET":
        get_newsfeed_settings = models.NewsfeedSettings.objects.filter(deleted=False).order_by("-id")
        return render(request, 'newsfeed_settings.html', { "get_newsfeed_settings": get_newsfeed_settings})
    elif request.method == "POST":
        country_of_news  = request.POST.get("country_of_news").strip()
        source_of_news   = request.POST.get("source_of_news").strip()
        keywords_of_news = request.POST.get("keywords_of_news").strip()

        models.NewsfeedSettings.objects.get_or_create(
            user_id=request.user.id, country=country_of_news, news_source=source_of_news, news_keyword=keywords_of_news
        )
        messages.success(request, "Newsfeed settings successfully added")
        
        return redirect("newsfeed_settings")
