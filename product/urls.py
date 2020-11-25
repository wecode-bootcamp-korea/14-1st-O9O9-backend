from django.urls import path
from product.views import CategoriesView, ProductsView, ProductDetailView, WatchListView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('/categories', ProductsView.as_view()),
    path('/categories/<int:product_id>', ProductDetailView.as_view()),
    path('/categories/watchlist', WatchListView.as_view())
]
