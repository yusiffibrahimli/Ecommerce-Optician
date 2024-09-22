from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.urls import reverse_lazy,reverse

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib import messages

class CustomRegisterView(CreateView):
    template_name = 'register.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomRegisterView,self).dispatch(request, *args, **kwargs)
   

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomUserLoginForm


class ForgetPasswordView(PasswordResetView):
    email_template_name="password_message.html"
    template_name = "forget_password.html"
    success_url = reverse_lazy("login")

    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ForgetPasswordView, self).get_success_url()
    
   
class ResetPasswordView(PasswordResetConfirmView):
    template_name = "reset_password.html"
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        print("Form is valid. Redirecting to login...")
        messages.success(self.request, 'Your password has been successfully changed. Please log in with your new password.')
        return super(ResetPasswordView,self).form_valid(form)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(CustomPasswordChangeView, self).get_success_url()



def my_account(request):
    return render(request, 'my-account.html')
 
# def login(request):
#     return render(request, 'login.html')


# def forget_password(request):
#     return render(request, 'forget_password.html')


