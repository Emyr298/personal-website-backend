from django.shortcuts import render
from django.http import JsonResponse
from django.middleware import csrf

# Create your views here.
def get_csrf_token(request):
    return JsonResponse({
        'csrf-token': csrf.get_token(request),
    })