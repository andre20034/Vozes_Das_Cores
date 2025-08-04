# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('signup/', views.signup, name='signup'), 
]