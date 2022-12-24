from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data.get('username')
        password = data.get('password')
        if username is not None and password is not None:
            try:
                user = User.objects.create_user(username=username, password=password)
                user_token = Token.objects.create(user=user)
                return JsonResponse({'token': user_token.key}, status=201)
            except Exception:
                return HttpResponse(status=400)
    return HttpResponse(status=403)