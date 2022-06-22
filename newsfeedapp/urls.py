from django.urls import path
from newsfeedapp import views

urlpatterns = [ 
    path('', views.user_login, name="user_login"),
    path('signup/', views.signup, name="signup"),
    path('user-logout/', views.user_logout, name="user_logout"),
    path('reset-password/', views.reset_password, name="reset_password"),
    path('newsfeed-settings/', views.newsfeed_settings, name="newsfeed_settings"),
    path('home/', views.home, name="home"),
    path('home/details/', views.details, name="details"),
]