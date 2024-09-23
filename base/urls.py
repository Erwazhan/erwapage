from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name='room'),
    path('test/', views.home, name='test'),
    path('navbar/', views.navbar, name='navbar'),
    path('contact/', views.contact, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

