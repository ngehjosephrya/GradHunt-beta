from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
import time

class HomeView(LoginRequiredMixin, View):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)
class DebugView(TemplateView):
    template_name = 'debug.html'
class LogoutView(LoginRequiredMixin, TemplateView):
    success_url =reverse_lazy('user_auth:login')
    def get(self, request):
        time.sleep(2)
        logout(request)
        return redirect(self.success_url) 
# Create your views here.
