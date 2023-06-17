
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.


def main(request):
    return render(request, "main.html")

@login_required
def home(request):
    # Logic for the home page
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Authentication failed, show an error message or handle it as needed
            pass
    return render(request, 'login.html')


def profile(request):
    # Logic for the profile page
    try:
        context = {
            'userExtracurriculars': request.user.studentprofile.extracurriculars,
            'userIsStudent': request.user.studentprofile,
            'userInterests': request.user.studentprofile.interests,
            'userIntrovertedExtroverted': request.user.studentprofile.introverted_extroverted,
            'userWhoYouAre': request.user.studentprofile.who_you_are,
            'userCountyInCalifornia': request.user.studentprofile.county_in_california,
            'userFutureCareerAspirations': request.user.studentprofile.future_career_aspirations,


        }
    except:
        context = {
            'userExtracurriculars': False,
        }
    return render(request, 'profile.html', context)