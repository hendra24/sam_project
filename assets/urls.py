from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('gardu/', views.all_gardu, name='all_gardu'),
    path('gardu/create_gardu/', views.create_gardu, name='create_gardu'),
    path('gardu/<str:gardu_name>/', views.detail_gardu, name='detail_gardu'),
    path('gardu/<int:id>/edit/', views.edit_gardu, name='edit_gardu'),  
    path('gardu/<str:gardu_name>/delete/', views.delete_gardu, name='delete_gardu'), 
    
    path('rtu/', views.all_rtu, name='all_rtu'),
    path('rtu/create_rtu/', views.create_rtu, name='create_rtu'),
    path('rtu/<int:id>/', views.detail_rtu, name='detail_rtu'), # pakai id karna rtu belum tentu di assign ke gardu
    path('rtu/<int:id>/edit/', views.edit_rtu, name='edit_rtu'),  
    path('rtu/<int:id>/delete/', views.delete_rtu, name='delete_rtu'),  
    
    path('rectifier/', views.all_rectifier, name='all_rectifier'),
    path('rectifier/create_rectifier/', views.create_rectifier, name='create_rectifier'),
    path('rectifier/<int:id>/', views.detail_rectifier, name='detail_rectifier'), # pakai id karna rectifier belum tentu di assign ke gardu
    path('rectifier/<int:id>/edit/', views.edit_rectifier, name='edit_rectifier'),  
    path('rectifier/<int:id>/delete/', views.delete_rectifier, name='delete_rectifier'),  
    
    path('media/', views.all_media, name='all_media'),
    path('media/create_media/', views.create_media, name='create_media'),
    path('media/<int:id>/', views.detail_media, name='detail_media'), # pakai id karna media belum tentu di assign ke gardu
    path('media/<int:id>/edit/', views.edit_media, name='edit_media'),  
    path('media/<int:id>/delete/', views.delete_media, name='delete_media'),
    
    path('fault_indicator/', views.all_fi, name='all_fi'),
    path('fault_indicator/create_media/', views.create_fi, name='create_fi'),
    path('fault_indicator/<int:id>/', views.detail_fi, name='detail_fi'), # pakai id karna media belum tentu di assign ke gardu
    path('fault_indicator/<int:id>/edit/', views.edit_fi, name='edit_fi'),  
    path('fault_indicator/<int:id>/delete/', views.delete_fi, name='delete_fi'),   
    
    path('inventory/rtu/', views.all_rtu, name='inventory_all_rtu'),
    path('inventory/rectifier/', views.all_rectifier, name='inventory_all_rectifier'),
    path('inventory/media/', views.all_media, name='inventory_all_media'),
    path('inventory/fault_indicator/', views.all_fi, name='inventory_all_fi'),
    path('inventory/move/<str:asset>/<int:id>', views.move_to_inventory, name='move_to_inventory'),
    
    path('cari/<str:asset>', views.cari, name='cari'),
   
   
    
    
    path('fi/', views.all_fi, name='all_fi'),
] 