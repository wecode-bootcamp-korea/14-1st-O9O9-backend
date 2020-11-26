from django.urls import path,include

urlpatterns = [
    path('user',include('user.urls')),
    path('review',include('review.urls')),
    path('order', include('order.urls')),
]
