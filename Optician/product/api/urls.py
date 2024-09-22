from django.urls import path, include
from .views import ProductVersionAPIView,ProductListView,ProductAPIView

urlpatterns = [
   path('products/', ProductListView.as_view(),name='products'),
   path('products/<int:pk>/', ProductAPIView.as_view(),name='product'),
   path('products/<product_id>/versions/',ProductVersionAPIView.as_view(),name='product-versions'),
   path('products/<product_id>/versions/<int:pk>/',ProductVersionAPIView.as_view(),name='product-version')
]



