from django.urls import path
from app_users_reg import views

urlpatterns = [
    # rota, view responsáel, nome de referência
    path('', views.home,name='home'),
    path('users/',views.users,name='users_list'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
