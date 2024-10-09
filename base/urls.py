from django.conf import settings
from django.conf.urls.static import static
from . import views
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name='room'),
    path('test/', views.home, name='test'),
    path('navbar/', views.navbar, name='navbar'),
    path('contact/', views.contact, name="contact"),
    path('tonestack/', views.tonestack, name="tonestack"),
    path('update-tone-response/', views.update_tone_response, name='update_tone_response'),  # For AJAX requests

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

