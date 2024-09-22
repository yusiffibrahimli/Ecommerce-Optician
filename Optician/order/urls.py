from django.urls import path
from .views import BasketView, checkout, WishlistView

urlpatterns = [
    path('basket/', BasketView.as_view(), name='basket'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
