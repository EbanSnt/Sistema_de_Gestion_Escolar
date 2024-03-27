from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('login',login, name='login'),
    path('sign_up', sign_up, name='sign_up'),
    path('permision_dennied', permision_dennied, name='permision_dennied'),
    path('login_required',permision_dennied_login,name='permision_dennied_login'),

]
