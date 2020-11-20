from django.urls import path
from .views import DoubleCheckView,SignUpView,SignInView
urlpatterns=[
    path('/doublecheck',DoubleCheckView.as_view()),
    path('/signupview',SignUpView.as_view()),
    path('/signinview',SignInView.as_view()),
]
