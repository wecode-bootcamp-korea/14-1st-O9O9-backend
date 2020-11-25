import json
import bcrypt
import jwt
import re
import string
import random
from django.views import View
from django.http import request, JsonResponse
from my_settings import SECRET
from .models import User,Allow
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

class DoubleCheckView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if re.match('^[a-zA-Z0-9]*$',data['ID']):
                if (len(data['ID'])>=6) and (len(data['ID'])<=10):
                    try:
                        if User.objects.get(username_id=data['ID']):
                            return JsonResponse({'message':'중복된 ID입니다'}, status=409)
                    except User.DoesNotExist:
                        return JsonResponse({'status':'success','message':'사용가능한 ID입니다'}, status=200)
                return JsonResponse({'message':'6~10자 사이의 영어 또는 숫자를 입력하세요'},status=400)
            return JsonResponse({'message':'영어 또는 숫자를 입력하세요'},status=400)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class SignUpCodeView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
                allow_code_length = 10
                string_pool = string.ascii_letters
                temporary_code = ''
                for i in range(allow_code_length):
                    temporary_code += random.choice(string_pool)

                user_email = data['email']
                user_name = data['name']
                msg_html = render_to_string('email/verify_email.html', {'temporary_code':temporary_code, 'user_name':user_name})
                msg = EmailMessage(
                subject="o9o9사이트 인증코드입니다 :)",
                body=msg_html,
                from_email='tmdwprpdla@gmail.com',
                bcc=[user_email]
                                )
                msg.content_subtype = 'html'
                msg.send()

                Allow.objects.create(allow_code = temporary_code)

                return JsonResponse({'message':'success'},status=200)

        except  KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class SignUpAllowView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Allow.objects.filter(allow_code = data['codeNumber']).exists():
                return JsonResponse({'message':'success'},status=200)
            return JsonResponse({'message':'unvalid AllowCode'})
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(username_id=data['ID']).exists():
                 return JsonResponse({'message':'아이디 중복확인을 하세요'},status=400)
            if not ((len(data['password'])>=6) and (len(data['password'])<=15)):
                return JsonResponse({'message':'6~15자 사이의 패스워드를 입력하세요'},status=400)
            form = re.compile('[a-zA-Z]+[0-9]+[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']?|[0-9]+[a-zA-Z]+[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']?|[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']?[a-zA-Z]+[0-9]+|[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']?[0-9]+[a-zA-z]+|[a-zA-Z]+[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']+[0-9]*|[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']+[a-zA-Z]+[0-9]*')

            if not form.match(data['password']):
                return JsonResponse({'message':'비밀번호는 영문 대/소문자,숫자 및 특수문자 2가지 이상의 조합으로 입력해야합니다'},status=400)
            if data['password'] != data['passwordcheck']:
                return JsonResponse({'message':'비밀번호가 일치하지 않습니다'},status=400)
            if not data['name'] :
                 return JsonResponse({'message':'이름을 입력해주세요'},status=400)
            if not data['phone_number'] :
                 return JsonResponse({'message':'휴대폰 번호를 정확히 입력해주세요'},status=400)
            if not data['email'] :
                 return JsonResponse({'message':'메일주소를 정확히 입력해주세요'},status=400)
            email_form = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

            if not email_form.match( data['email']) :
                 return JsonResponse({'message':'메일주소를 정확히 입력해주세요'},status=400)
            
            user_email = data['email']
            user_name = data['name']
            msg_html = render_to_string('email/send_email.html',{'user_name':user_name})
            msg = EmailMessage(
                                subject="o9o9 가입을 환영합니다 :)",
                                body=msg_html,
                                from_email='tmdwprpdla@gmail.com',
                                bcc=[user_email]
                              )
            msg.content_subtype = 'html'
            msg.send()

            encohash_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User.objects.create(username_id=data['ID'],
                                password=encohash_password.decode('utf-8'),
                                name=data['name'], 
                                phone_number=data['phone_number'], 
                                email_address=data['email'],)

            return JsonResponse({'message':'회원가입이 완료되었습니다'},status=200) 

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(username_id=data['ID']).exists():
                login_user = User.objects.get(username_id=data['ID'])
                inspect_passoword = bcrypt.checkpw(data['password'].encode('utf-8'),login_user.password.encode('utf-8'))

                if inspect_passoword:
                    access_token = jwt.encode({'id':login_user.id,},SECRET, algorithm='HS256')
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

class SignInName(View): # 유저의 토큰을 확인해서 이름을 보내주는 클래스

    def get(self, request,**kwargs):
        for_client_token = request.headers.get('authorization',None)
        if for_client_token is None:
            return JsonResponse({'message': 'token please'},status=400)
        try:
            user_id = jwt.decode(for_client_token, SECRET, algorithms='HS256')
            user = User.objects.get(id=user_id['id'])
            token_user_name = user.name
            return JsonResponse({'message':token_user_name},status=200)
        except User.DoesNotExist:
            return JsonResponse({'message':'unknown_user'},status=401)
        except jwt.DecodeError:
            return JsonResponse({'message':'invalid_token'},status=401)


