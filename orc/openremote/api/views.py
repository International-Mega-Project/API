from django.shortcuts import render
from .apps import ApiConfig

# Create your views here.
from django.http.response import Http404, HttpResponse, JsonResponse

import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


sampleData = {
    "12:00": "100",
    "13:00": "200",
    "14:00": "250",
    "15:00": "225",
    "16:00": "110",
    "17:00": "100",
    "18:00": "80",
    "19:00": "30",
    "20:00": "35",
    "21:00": "20",
    "22:00": "2",
}

@csrf_exempt
def get(request):
    # hourly post's
    if request.method != 'POST':
        raise Http404
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        response = JsonResponse(
            sampleData, status=200
        )
        return response
    except IntegrityError:
        return HttpResponse(
            json.dumps({"status": 201, "message": "user already exists , please try different user name "}),
            content_type='application/json')
    # if request.method == 'POST':
    #     params = request.POST.get()
    #
    #     # predict method used to get the prediction
    #     response = ApiConfig.predictor.predict()
    #
    #     # returning JSON response
    #     return JsonResponse(response)
