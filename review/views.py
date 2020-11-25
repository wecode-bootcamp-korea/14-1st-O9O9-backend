import json
from django.views import View
from django.http import request,JsonResponse
from user.models import User
from .models import Question
from .models import QuestionType
from .models import AnswerStatus
from product.models import Product
from datetime import datetime
from user.utils import check_user

class QuestionView(View):
    def get(self,request):
        questions = Question.objects.all()
        question_list = [
            {
                'number' : question.id,
                'question_type' : question.question_type.id,
                'answer_status' : question.answer_status.id,
                'title' : question.title,
                'content' : question.content,
                'question_man' : question.user.username_id,
                'created_at' : question.created_at
            } for question in questions
        ]
        return JsonResponse({'question_list':question_list},status=200)

class QuestionInfoView(View):
    @check_user
    def post(self, request):
        data = json.loads(request.body)
        login_user = User.objects.get(id = request.user)
        product_name = Product.objects.get(name = data['product_name'])
        return JsonResponse({'name':login_user.name,
                             'email':login_user.email_address,
                             'phone_number':login_user.phone_number,
                             'product_name':product_name.name},status=200)

class QuestionEnrollView(View):
    @check_user
    def post(self, request):
        try:
            data       = json.loads(request.body)
            login_user = User.objects.get(id = request.user)
            quest_type = QuestionType.objects.get(id=data["type"])
            answer = AnswerStatus.objects.get(id = data["answer"])
            product_name = Product.objects.get(name = data["product_name"])
            Question.objects.create(user          = login_user,
                                    product       = product_name,
                                    title         = data["title"],
                                    content       = data["content"],
                                    question_type = quest_type,
                                    answer_status = answer,
                                    created_at    = datetime.now(),)
            return JsonResponse({'message':'success'},status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=200)

class QuestionModifyView(View):
    @check_user
    def delete(self,request,question_number):
        try:
            question_delete = Question.objects.get(id=question_number)
            question_delete.delete()
            return JsonResponse({'message':'success'},status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=200)

    @check_user
    def get(self,request,question_number):
        try:
            login_user = User.objects.get(id = request.user)
            question   = Question.objects.get(id = question_number)
            return JsonResponse({'question_type':question.question_type.id ,
                                 'product_name':question.product.name,
                                 'name':login_user.name,
                                 'email':login_user.email_address,
                                 'phone_number':login_user.phone_number,
                                 'title':question.title,
                                 'content':question.content },status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=200)

    @check_user
    def put(self,request,question_number):
        try:
            data                 = json.loads(request.body)
            login_user           = User.objects.get(id = request.user)
            question_type        = QuestionType.objects.get(id=data['update_question_type'])
            quesiton_type_update =  Question.objects.filter(id = question_number).update(question_type = question_type,
                                                                                         title         = data['update_question_title'],
                                                                                         content       = data['update_question_content'])
           
            return JsonResponse({'message':'success'},status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)




