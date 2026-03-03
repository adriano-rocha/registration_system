from django.contrib import admin
from django.urls import path
from app_users_reg import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.users, name='users_list'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'), 
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]

# Serve media files em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)