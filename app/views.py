from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def test_api(request):
    return JsonResponse({"result": "success"})


def test_api2(request):
    return JsonResponse({"result": "success"})
