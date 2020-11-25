from django.urls import path
from .views import DoubleCheckView,SignUpView,SignInView,SignInName,SignUpAllowView,SignUpCodeView
urlpatterns=[
    path('/doublecheck',DoubleCheckView.as_view()),
    path('/signupallow',SignUpAllowView.as_view()),
    path('/signup',SignUpView.as_view()),
    path('/signin',SignInView.as_view()),
    path('/name',SignInName.as_view()),
    path('/signupcode',SignUpCodeView.as_view()),
]
