from django.urls import path
from product.views import CategoriesView, ProductsView, ProductDetailView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('/categories', ProductsView.as_view()),
    path('/categories/<int:product_id>', ProductDetailView.as_view())
]
