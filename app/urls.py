from django.urls import path
from . import views
# from .Engines.responses import *


urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]