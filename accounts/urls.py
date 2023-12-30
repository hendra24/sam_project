from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete_image', views.remove_profile_image, name='delete_image')
] 