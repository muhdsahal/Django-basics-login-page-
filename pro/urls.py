from django.contrib import admin
from django.urls import path,include
from . import views
from .views import home,user_login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
  
   path('', views.user_login, name="user_login"),
   path('home/', views.home, name="home"),
   path("logout_user", views.logout_user, name="logout_user"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)