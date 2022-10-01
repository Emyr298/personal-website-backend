from django.http import JsonResponse
from django.core import serializers

class Status:
    SUCCESS = 'success'
    FAIL = 'fail'
    ERROR = 'error'

def success(data, status_code):
    response_data = {
        'status': Status.SUCCESS,
        'data': data,
    }
    return JsonResponse(response_data, status=status_code)

def error(message, status_code):
    response_data = {
        'status': Status.ERROR,
        'message': message,
    }
    return JsonResponse(response_data, status=status_code)
