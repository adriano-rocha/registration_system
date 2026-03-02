from django.urls import path
from app_users_reg import views

urlpatterns = [
    # rota, view responsáel, nome de referência
    path('', views.home,name='home')
]
