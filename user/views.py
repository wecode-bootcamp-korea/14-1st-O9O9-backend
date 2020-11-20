import json
import bcrypt
import jwt
import re
from django.views import View
from django.http import request,JsonResponse
from my_settings import SECRET
from .models import User,CheckId
#{ID:psj0810, password:12345, password_check:12345, name:박승제, phone_number:010-123-1234, email:}


class DoubleCheckView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if re.match('^[a-zA-Z0-9]*$',data['ID']):
                if (len(data['ID'])>=6) and (len(data['ID'])<=10):
                    try:
                        if User.objects.get(username_id=data['ID']):
                            return JsonResponse({'message':'중복된 ID입니다'}, status=400)
                    except User.DoesNotExist:
                            CheckId.objects.create(checkid=data['ID'])
                            return JsonResponse({'message':'success'}, status=200)
                return JsonResponse({'message':'6~10자 사이의 영어 또는 숫자를 입력하세요'},status=400)
            return JsonResponse({'message':'영어 또는 숫자를 입력하세요'},status=400)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:

            if CheckId.objects.filter(checkid=data['ID']).exists()==False:
                return JsonResponse({'message':'아이디 중복확인을 하세요'},status=400)
            if ((len(data['password'])>=6) and (len(data['password'])<=15))==False:
            	return JsonResponse({'message':'6~15자 사이의 패스워드를 입력하세요'},status=400)
            if re.match('^[a-zA-Z0-9]*$',data['password'])==False or re.match('^[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…a-zA-Z]*$',data['password'])==False:
            	return JsonResponse({'message':'비밀번호는 영문 대/소문자,숫자 및 특수문자 2가지 이상의 조합으로 입력해야합니다'},status=400)
            if data['password'] != data['passwordcheck']:
               return JsonResponse({'message':'비밀번호가 일치하지않습니다'},status=400)
            if data['name'] == '':
                return JsonResponse({'message':'이름을 입력해주세요'},status=400)
            if data['phone_number'] == '':
                return JsonResponse({'message':'휴대폰 번호를 정확히 입력해주세요'},status=400)
            if data['email'] == '':
                return JsonResponse({'message':'메일주소를 정확히 입력해주세요'},status=400)
            if '@' not in data['email']:
                return JsonResponse({'message':'메일주소를 정확히 입력해주세요'},status=400)
            if '.' not in data['email']:
                return JsonResponse({'message':'메일주소를 정확히 입력해주세요'},status=400)

            if CheckId.objects.filter(checkid=data['ID']).exists():
               pass 
            if (len(data['password'])>=6) and (len(data['password'])<=15):
                pass	
            if re.match('^[a-zA-Z0-9]*$',data['password']) or re.match('^[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…a-zA-Z0-9]*$',data['password']):
            	pass
            if data['password'] == data['passwordcheck']:

                encohash_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

                User.objects.create(username_id=data['ID'],
                                    password=encohash_password.decode('utf-8'),
                                    name=data['name'], 
                                    phone_number=data['phone_number'], 
                                    email_address=data['email'],)
            return JsonResponse({'message':'success'},status=200)

        except  KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(username_id=data['ID']).exists():
                login_user = User.objects.get(username_id=data['ID'])
                inspect_passoword = bcrypt.checkpw(data['password'].encode('utf-8'),login_user.password.encode('utf-8'))
                if inspect_passoword == True:
                    access_token = jwt.encode({'id':login_user.id},SECRET, algorithm='HS256')
                    for_client_token = access_token.decode('utf-8')
                    return JsonResponse({'authorization':for_client_token}, status=200)
                else: return JsonResponse({'message':'비밀번호가 일치하지 않습니다'},status=400)

                if data['password'] == '':
                    return JsonResponse({'message':'패스워드를 입력하세요'},status=400)
            return JsonResponse({'message':'존재하지 않는 ID입니다'},status=400)
                
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)
        except  User.DoesNotExist:
            return JsonResponse({'message':'존재하지않는 ID입니다'},status=400)


