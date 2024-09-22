from django.urls import path
from .views import about, IndexView, SearchView, subscribe
 
urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('about/', about, name='about'),
    path('contact/', about, name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('',IndexView.as_view(),name="index"),
]

 