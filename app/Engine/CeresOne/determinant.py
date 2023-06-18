import json
from django.http import JsonResponse
from django.http import HttpResponse
from ..Launchpad.OPENAI_CONNECTOR import getResponse

variable_names = [
    'Admiration',
    'Adoration',
    'Aesthetic Appreciation',
    'Amusement',
    'Anger',
    'Annoyance',
    'Anxiety',
    'Awe',
    'Awkwardness',
    'Boredom',
    'Calmness',
    'Concentration',
    'Confusion',
    'Contemplation',
    'Contempt',
    'Contentment',
    'Craving',
    'Determination',
    'Disappointment',
    'Disapproval',
    'Disgust',
    'Distress',
    'Doubt',
    'Ecstasy',
    'Embarrassment',
    'Empathic Pain',
    'Enthusiasm',
    'Entrancement',
    'Envy',
    'Excitement',
    'Fear',
    'Gratitude',
    'Guilt',
    'Horror',
    'Interest',
    'Joy',
    'Love',
    'Nostalgia',
    'Pain',
    'Pride',
    'Realization',
    'Relief',
    'Romance',
    'Sadness',
    'Sarcasm',
    'Satisfaction',
    'Desire',
    'Shame',
    'Surprise (negative)',
    'Surprise (positive)',
    'Sympathy',
    'Tiredness',
    'Triumph'
]

def GET_SENTENCE_RECOMMENDATION(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence', '')
        name = request.POST.get('name', '')

        # Perform necessary processing based on the received sentence and name

        print(name)

        issues = []
        for num in name:
            issues.append(int(num))

        #remove duplicates
        issues = list(dict.fromkeys(issues))



        real_issues = []

        for x in issues:
            real_issues.append(variable_names[x])


        prompt = f"Given the following sentence, and list of \"LACK OF SENTIMENTS\"\n\nSENTENCE: {sentence}\n\n\nSENTIMENTS MISSING: {real_issues}\n\nGive me tips on how to improve the sentence without generating any sentence content directly.\n\n"
        temperature = 1
        max_tokens = 256
        top_p = 1
        frequency_penalty = 0
        presence_penalty = 0

        sentenceResponse = getResponse(prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)




        sentence_response = {
            'sentence': sentenceResponse,
            'name': name
        }

        return JsonResponse(sentence_response)

    return HttpResponse(status=405)  # Return a proper response for other request methods
