# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
=======
    path('', views.homePageView, name='home')
>>>>>>> 171f531816a2bab6ba61924e93f9b7a677a82750
]
