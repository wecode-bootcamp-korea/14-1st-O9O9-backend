from django.urls import path

from .views      import OrderView, OrderDeleteView

urlpatterns = [
    path('/', OrderView.as_view()),
    path('/<int:product_id>', OrderView.as_view()),
    path('/cart', OrderDeleteView.as_view()),
]