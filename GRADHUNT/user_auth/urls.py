from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView
app_name='user_auth'
urlpatterns = [
    path('',RegistrationView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('forgot_password/', ForgotPasswordView.as_view(),name='forgot_password'),
    path('reset_password/',RecoverPasswordView.as_view(),name='reset_password'),
    path('debug/', DebugView.as_view(),name='debug'),
    
]
