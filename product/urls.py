from django.urls import path
from .views import ProductSearch

urlpatterns=[
    path('/productsearch',ProductSearch.as_view())
]
