from django.urls import path
from . import views
# from .views import login_view, logout_view
# from .Engines.responses import *


urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.home, name="home"),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]