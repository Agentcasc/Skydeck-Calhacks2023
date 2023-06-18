from django.shortcuts import render


def save_profile_data(request):
    if request.method == 'POST':
        # Retrieve form data
        extracurriculars = request.POST.get('extracurriculars')
        introverted_extroverted = request.POST.get('introverted_extroverted')
        interests = request.POST.get('interests')
        who_you_are = request.POST.get('who_you_are')
        county_in_california = request.POST.get('county_in_california')
        future_career_aspirations = request.POST.get('future_career_aspirations')

        # Convert "Yes" and "No" to True and False
        work_indoors = request.POST.get('work_indoors') == 'yes'
        work_outdoors = request.POST.get('work_outdoors') == 'yes'
        fast_paced_environment = request.POST.get('fast_paced_environment') == 'yes'
        relaxed_environment = request.POST.get('relaxed_environment') == 'yes'
        collaborative_team = request.POST.get('collaborative_team') == 'yes'
        independent_work = request.POST.get('independent_work') == 'yes'
        physically_demanding_work = request.POST.get('physically_demanding_work') == 'yes'
        willing_to_travel = request.POST.get('willing_to_travel') == 'yes'
        flexible_work_hours = request.POST.get('flexible_work_hours') == 'yes'
        structured_environment = request.POST.get('structured_environment') == 'yes'
        casual_environment = request.POST.get('casual_environment') == 'yes'
        competitive_atmosphere = request.POST.get('competitive_atmosphere') == 'yes'
        supportive_atmosphere = request.POST.get('supportive_atmosphere') == 'yes'
        job_variety = request.POST.get('job_variety') == 'yes'
        routine_oriented = request.POST.get('routine_oriented') == 'yes'
        customer_interaction = request.POST.get('customer_interaction') == 'yes'
        work_life_balance = request.POST.get('work_life_balance') == 'yes'
        comfortable_with_technology = request.POST.get('comfortable_with_technology') == 'yes'
        open_to_learning = request.POST.get('open_to_learning') == 'yes'




        # Update data in the database
        student_profile = request.user.studentprofile
        student_profile.extracurriculars = extracurriculars
        student_profile.introverted_extroverted = introverted_extroverted
        student_profile.interests = interests
        student_profile.who_you_are = who_you_are
        student_profile.county_in_california = county_in_california
        student_profile.future_career_aspirations = future_career_aspirations

        student_profile.work_indoors = work_indoors
        student_profile.work_outdoors = work_outdoors
        student_profile.fast_paced_environment = fast_paced_environment
        student_profile.relaxed_environment = relaxed_environment
        student_profile.collaborative_team = collaborative_team
        student_profile.independent_work = independent_work
        student_profile.physically_demanding_work = physically_demanding_work
        student_profile.willing_to_travel = willing_to_travel
        student_profile.flexible_work_hours = flexible_work_hours
        student_profile.structured_environment = structured_environment
        student_profile.casual_environment = casual_environment
        student_profile.competitive_atmosphere = competitive_atmosphere
        student_profile.supportive_atmosphere = supportive_atmosphere
        student_profile.job_variety = job_variety
        student_profile.routine_oriented = routine_oriented
        student_profile.customer_interaction = customer_interaction
        student_profile.work_life_balance = work_life_balance
        student_profile.comfortable_with_technology = comfortable_with_technology
        student_profile.open_to_learning = open_to_learning

        student_profile.save()

        # Perform further processing or save the data to the database
        print('SUCCESS')

        # Redirect to a success page or perform any other necessary actions
        context = {
            'userExtracurriculars': student_profile.extracurriculars,
            'userIsStudent': student_profile,
            'userInterests': student_profile.interests,
            'userIntrovertedExtroverted': student_profile.introverted_extroverted,
            'userWhoYouAre': student_profile.who_you_are,
            'userCountyInCalifornia': student_profile.county_in_california,
            'userFutureCareerAspirations': student_profile.future_career_aspirations,
        }

        return render(request, 'profile.html', context)

    # Render the form initially or handle other HTTP methods
    return render(request, 'profile.html')


def save_student_workpreferences(request):
    ...