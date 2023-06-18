from django.urls import path
from . import views
# from .Engines.responses import *
from .CRUD import update


urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    #save-profile-data
    path('save-profile-data/', update.save_profile_data, name='save-profile-data'),
    path('workpreferences/', views.workpreferences, name='workpreferences'),
    path('development_planning/', views.development_planning, name='development_planning'),
]