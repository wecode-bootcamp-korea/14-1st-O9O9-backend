from django.urls import path
from .views import DoubleCheckView,SignUpView,SignInView
urlpatterns=[
    path('/doublecheck',DoubleCheckView.as_view()),
    path('/signup',SignUpView.as_view()),
    path('/signin',SignInView.as_view()),
]
