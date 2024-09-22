from django.urls import path
from .views import WishListAPIView, BasketAPIView

urlpatterns = [
    path('wishlist/', WishListAPIView.as_view(), name='api_wishlist'),
    path('basket/', BasketAPIView.as_view(), name='api_basket'),
]