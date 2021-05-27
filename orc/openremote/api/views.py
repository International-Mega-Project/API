from django.shortcuts import render
from .apps import ApiConfig

# Create your views here.
from django.http.response import Http404, HttpResponse, JsonResponse

import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


@csrf_exempt
def get(request):
    # hourly post's
    if request.method != 'POST':
        raise Http404
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        response = JsonResponse(
            body, status=200
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
