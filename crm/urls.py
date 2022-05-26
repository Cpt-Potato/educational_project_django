from django.urls import path

from . import views

urlpatterns = [
    path('thanks/', views.thanks_page, name='thanks'),
    path('', views.index)
]
