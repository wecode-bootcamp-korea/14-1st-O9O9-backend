from django.urls import path
from product.views import CategoriesView, ProductsView, ProductDetailView, WatchListView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/categories', CategoriesView.as_view()),
    path('/watchlist', WatchListView.as_view())
]
