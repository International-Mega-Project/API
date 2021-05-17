from django.shortcuts import render
from .apps import ApiConfig

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def get(request):
    if request.method == 'GET':
        params = request.GET.get('prediction-data')

        # predict method used to get the prediction
        response = ApiConfig.predictor.predict()

        # returning JSON response
        return JsonResponse(response)
