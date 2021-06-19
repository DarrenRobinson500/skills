from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.people_list, name='people_list'),

    path('people_list', views.people_list, name='people_list'),
    path('people_ind/<id>', views.people_ind, name='people_ind'),
    path('people_skill_update/<people_id>/<sub_category_id>/<level_id>', views.people_skill_update, name='people_skill_update'),
    path('people_target_update/<people_id>/<sub_category_id>/<level_id>', views.people_target_update, name='people_target_update'),
    path('people_upload/<id>', views.people_upload, name='people_upload'),
    path('people_update/<id>', views.people_update, name='people_update'),
    path('people_delete/<id>', views.people_delete, name='people_delete'),
    path('people_delete_all', views.people_delete_all, name='people_delete_all'),

    path('skill_list', views.skill_list, name='skill_list'),
    path('skill_ind/<sub_category_id>/<level_id>', views.skill_ind, name='skill_ind'),
    path('skill_cat_upload/<id>', views.skill_cat_upload, name='skill_cat_upload'),
    path('skill_upload/<id>', views.skill_upload, name='skill_upload'),
    path('skill_update/<id>', views.skill_update, name='skill_update'),
    path('skill_delete/<id>', views.skill_delete, name='skill_delete'),
    path('skill_delete_all', views.skill_delete_all, name='skill_delete_all'),

    path('file_list', views.file_list, name='file_list'),
    path('file_upload', views.file_upload, name='file_upload'),
    path('file_delete/<file_id>', views.file_delete, name='file_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
