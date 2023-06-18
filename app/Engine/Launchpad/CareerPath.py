from .OPENAI_CONNECTOR import getResponse
from django.http import HttpResponse
from django.shortcuts import render

def response(request):
    if request.method == 'POST':

        extracurriculars = request.user.studentprofile.extracurriculars
        interests = request.user.studentprofile.interests
        introverted_extroverted = request.user.studentprofile.introverted_extroverted
        who_you_are = request.user.studentprofile.who_you_are
        county_in_california = request.user.studentprofile.county_in_california
        future_career_aspirations = request.user.studentprofile.future_career_aspirations

        work_indoors = request.user.studentprofile.work_indoors
        work_outdoors = request.user.studentprofile.work_outdoors
        fast_paced_environment = request.user.studentprofile.fast_paced_environment
        relaxed_environment = request.user.studentprofile.relaxed_environment
        collaborative_team = request.user.studentprofile.collaborative_team
        independent_work = request.user.studentprofile.independent_work
        physically_demanding_work = request.user.studentprofile.physically_demanding_work
        willing_to_travel = request.user.studentprofile.willing_to_travel
        flexible_work_hours = request.user.studentprofile.flexible_work_hours
        structured_environment = request.user.studentprofile.structured_environment
        casual_environment = request.user.studentprofile.casual_environment
        competitive_atmosphere = request.user.studentprofile.competitive_atmosphere
        supportive_atmosphere = request.user.studentprofile.supportive_atmosphere
        job_variety = request.user.studentprofile.job_variety
        routine_oriented = request.user.studentprofile.routine_oriented
        customer_interaction = request.user.studentprofile.customer_interaction
        work_life_balance = request.user.studentprofile.work_life_balance
        comfortable_with_technology = request.user.studentprofile.comfortable_with_technology
        open_to_learning = request.user.studentprofile.open_to_learning

        prompt = f"Given a student profile where the grade level is 9-12, find a suitable career path based on the following responses:\n\nExtracurriculars: {extracurriculars}\n\nIntroverted extroverted: {introverted_extroverted}\n\nInterests: {interests}\n\nWho you are: {who_you_are}\n\nCounty in California: {county_in_california}\n\nFuture career aspirations: {future_career_aspirations}\n\nWork indoors: {work_indoors}\n\nWork outdoors: {work_outdoors}\n\nFast paced environment: {fast_paced_environment}\n\nRelaxed environment: {relaxed_environment}\n\nCollaborative team: {collaborative_team}\n\nIndependent work: {independent_work}\n\nPhysically demanding work: {physically_demanding_work}\n\nWilling to travel: {willing_to_travel}\n\nFlexible work hours: {flexible_work_hours}\n\nStructured environment: {structured_environment}\n\nCasual environment: {casual_environment}\n\nCompetitive atmosphere: {competitive_atmosphere}\n\nSupportive atmosphere: {supportive_atmosphere}\n\nJob variety: {job_variety}\n\nRoutine oriented: {routine_oriented}\n\nCustomer interaction: {customer_interaction}\n\nWork life balance: {work_life_balance}\n\nComfortable with technology: {comfortable_with_technology}\n\nOpen to learning: {open_to_learning}\n\nGive me 5 careers, along with their descriptions that suit the given student profile --> IN A NUMBERED FORMAT WHERE EACH CAREER IS SEPARATED BY NEWLINES\n\n"
        temperature = 1
        max_tokens = 500
        top_p = 1
        frequency_penalty = 0
        presence_penalty = 0
        response = getResponse(prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)
        print(response)

        #response is parsable as each career is separated by a number
        response = response.split("\n")
        #remove elements where the length is 0
        response = [x for x in response if len(x) != 0]

        career1 = response[0]
        career2 = response[1]
        career3 = response[2]
        career4 = response[3]
        career5 = response[4]

        context = {
            'career1': career1,
            'career2': career2,
            'career3': career3,
            'career4': career4,
            'career5': career5,
        }


    return render(request, 'development_planning.html', context)
