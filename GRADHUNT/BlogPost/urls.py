from django.urls import path
from .views import *

app_name = 'BlogPost'
urlpatterns = [
    
    path('blog/', IndexView.as_view() , name='blogpost'),
]