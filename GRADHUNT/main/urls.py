from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('debug/', DebugView.as_view(),name='debug'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)