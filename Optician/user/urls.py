from django.urls import path
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView

from .views import CustomRegisterView, CustomLoginView, ForgetPasswordView, ResetPasswordView, CustomPasswordChangeView
from . import views
 
urlpatterns = [
    path('myaccount/', views.my_account, name='my_account'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('change_password/', CustomPasswordChangeView.as_view(), name = "change_password"),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),
]