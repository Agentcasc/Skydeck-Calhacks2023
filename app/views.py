
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


def login_view(request):
    error_message = None  # Assign a default value to error_message

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password. Please try again.'

    return render(request, 'login.html', {'error_message': error_message})


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


def workpreferences(request):
    return render(request, 'workpreferences.html')


def development_planning(request):
    if request.user.studentprofile.chosenCareerField != None or request.user.studentprofile.chosenCareerField != "":
        chosen = request.user.studentprofile.chosenCareerField
        print(chosen)
        context = {
            "career1": "",
            "career2": "",
            "career3": "",
            "career4": "",
            "career5": "",
            "chosen": chosen,
            "isChosen": True,
        }
        print(context)

    else:
        context = {
            "career1": "",
            "career2": "",
            "career3": "",
            "career4": "",
            "career5": "",
            "chosenField": ""
        }
    return render(request, 'development_planning.html',context)


def CeresOne(request):
    return render(request, 'CeresOne.html')