from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('customsearch/', views.index, name='index'),
    path('about/', views.about, name='about'),
]