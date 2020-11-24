from django.urls import path

from .views      import OrderView

urlpatterns = [
    path('/', OrderView.as_view()),
    path('/<int:cart_id>', OrderView.as_view())
]