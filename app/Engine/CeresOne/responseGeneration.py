import random
import re
import json
from django.http import HttpResponse


def essayResponse(request):
    essay = request.POST.get('essay', '')  # Get the essay content from the POST request

    # Split the essay into sentences based on periods, exclamation marks, and question marks
    sentences = re.split(r'(?<=[.!?])\s+', essay)

    sentence_responses = []

    for sentence in sentences:
        label = random.choice(["good", "not-good"])
        sentence_response = {
            'sentence': sentence,
            'label': label
        }
        sentence_responses.append(sentence_response)

    # Convert the sentence_responses list to JSON format
    json_response = json.dumps(sentence_responses)

    # Set the content type of the HTTP response to application/json
    response = HttpResponse(json_response, content_type='application/json')

    return response
