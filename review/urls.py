from django.urls import path
from .views import QuestionView, QuestionInfoView, QuestionEnrollView,QuestionModifyView
urlpatterns=[
    path('/question', QuestionView.as_view()),
    path('/questioninfo',QuestionInfoView.as_view()),
    path('/questionenroll',QuestionEnrollView.as_view()),
    path('/question/<int:question_number>',QuestionModifyView.as_view()),
]
