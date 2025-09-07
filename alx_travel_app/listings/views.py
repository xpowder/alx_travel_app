from django.shortcuts import render

from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "ALX Travel API is working!"})
