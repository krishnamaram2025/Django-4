from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),

]