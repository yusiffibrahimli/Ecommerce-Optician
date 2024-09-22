from django.urls import path
from blog.views import blog, blog_details, contact

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog-details/<int:pk>/', blog_details, name='blog-details'),
    path('contact/', contact, name='contact'),
]