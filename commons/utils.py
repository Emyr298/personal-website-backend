from django.http import JsonResponse

class ResponseFormatter:
    class Status:
        SUCCESS = 'success'
        FAIL = 'fail'
        ERROR = 'error'

    def success(data, status_code):
        response_data = {
            'status': ResponseFormatter.Status.SUCCESS,
            'data': data,
        }
        return JsonResponse(response_data, status=status_code)
    
    def fail(data, message, status_code):
        response_data = {
            'status': ResponseFormatter.Status.FAIL,
            'data': data,
            'message': message,
        }
        return JsonResponse(response_data, status=status_code)

    def error(message, status_code):
        response_data = {
            'status': ResponseFormatter.Status.SUCCESS,
            'message': message,
        }
        return JsonResponse(response_data, status=status_code)
