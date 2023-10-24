from django.views.generic import TemplateView
from .models import *
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView,PasswordChangeView
from django.contrib import admin

class RegistrationView(View):
    template_name = 'registration.html'
    success_url = 'user_auth:login'  
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        data = request.POST
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        gender = data['gender']
        speciality = data['speciality']
        contact = data['contact']
        password = data['password1']
        hashed_password = make_password(password)
        try:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            student = Student(username=username, first_name=firstname, last_name=lastname, email=email, password=hashed_password, contact=contact, speciality=speciality, gender=gender)  
            student.save()
            user.save()
            return redirect(self.success_url)
        except Exception as e:  
            print("Error:", str(e)) 
        return redirect(self.template_name) 
class LoginView(View):
    template_name = 'login.html'
    success_url = reverse_lazy('main:home')
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        data = request.POST
        username = data.get("username")
        password = data.get("password1")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name)
class DebugView(TemplateView):
    template_name = 'debug.html'
class ForgotPasswordView(PasswordResetView):
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('user_auth:reset_password')
class RecoverPasswordView(PasswordChangeView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('user_auth:login')

    