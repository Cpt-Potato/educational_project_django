from django.urls import path

from . import views

urlpatterns = [
    path('thanks/', views.thanks, name='thanks'),
    path('', views.index, name='index')
]
