from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
import os

@csrf_exempt
def healthcheck(request):
    return HttpResponse("OK", status=200)