from django.shortcuts import render
from .apps import ApiConfig

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http.response import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ironman.models import *
import json
from django.template import RequestContext
from dashboard.models import PromoCluster, Beacon
from datetime import datetime
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *
from django.contrib.gis.geos.factory import fromstr
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth import logout


@csrf_exempt
def signup(request):
    if request.method != 'POST':
        raise Http404
    email = request.POST.get('email')
    try:

        return HttpResponse(json.dumps({"status": 200}), content_type='application/json')
    except IntegrityError:
        return HttpResponse(
            json.dumps({"status": 201, "message": "user already exists , please try different user name "}),
            content_type='application/json')


def get(request):
    if request.method == 'POST':
        params = request.POST.get()

        # predict method used to get the prediction
        response = ApiConfig.predictor.predict()

        # returning JSON response
        return JsonResponse(response)
