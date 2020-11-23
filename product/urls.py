from django.urls import path
from product.views import CategoryView, ProductListView, SubCategoryView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('/Category/<int:maincategory_id>', ProductListView.as_view()),
    path('/Category/<int:maincategory_id>/<int:subcategory_id>', SubCategoryView.as_view()),
]
