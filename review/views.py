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
                'number' : question.user.id,
                'question_type' : question.question_type.id,
                'answer_status' : question.answer_status.id,
                'title' : question.title,
                'question_man' : question.user.username_id,
                'created_at' : question.created_at
            } for question in questions
        ]
        return JsonResponse({'question_list':question_list},status=200)

class QuestionInfoView(View):
    @check_user
    def get(self, request):
        data = json.loads(request.body)
        login_user = User.objects.get(id = request.user)
        product_name = Product.objects.get(name = data['temporary_key'])
        return JsonResponse({'name':login_user.name,'email':login_user.email_address,'phone_number':login_user.phone_number,'product_name':product_name.name},status=200)

class QuestionEnrollView(View):
    @check_user
    def post(self, request):
        try:
            data       = json.loads(request.body)
            login_user = User.objects.get(id = request.user)
            quest_type = QuestionType.objects.get(id=data["type"])
            answer = AnswerStatus.objects.get(id = data["answer"])
            product_name = Product.objects.get(name = data["temporary_key"])
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
