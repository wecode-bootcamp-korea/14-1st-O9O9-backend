import jwt
from django.http import request,JsonResponse
from my_settings import SECRET
from user.models import User

def check_user(func):
    def wrapper_func(self, request):
        for_client_token = request.headers.get('authorization',None)
        if for_client_token is None:
            return JsonResponse({'message': 'token please'},status=400)
        try:
            user_id = jwt.decode(for_client_token, SECRET, algorithms='HS256')
            user = User.objects.get(id=user_id['id'])
            request.user = user.id
            return func(self,request)
        except User.DoesNotExist:
            return JsonResponse({'message':'unknown_user'},status=401)
        except jwt.DecodeError:
            return JsonResponse({'message':'invalid_token'},status=401)
    return wrapper_func
