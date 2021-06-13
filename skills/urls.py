from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.people_list, name='people_list'),
    path('people_list', views.people_list, name='people_list'),
    path('skill_list', views.skill_list, name='skill_list'),
    path('skill_upload', views.skill_upload, name='skill_upload'),
    path('file_list', views.file_list, name='file_list'),
    path('file_upload', views.file_upload, name='file_upload'),
    path('file_delete/<file_id>', views.file_delete, name='file_delete'),
]
