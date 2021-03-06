from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
import tinymce


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.notes_list, name='notes_list'),
    path('calendar', views.calendar, name='calendar'),
    path('life', views.life, name='life'),
    path('new_mindmap', views.new_mindmap, name='new_mindmap'),
    path('new_mindmap/<id>', views.new_mindmap, name='new_mindmap'),
    path('new_map_item/<type>/<map_id>', views.new_map_item, name='new_map_item'),
    path('new_map_item/<type>/<map_id>/<selected_id>', views.new_map_item, name='new_map_item'),
    path('delete_node/<map_id>/<id>', views.delete_node, name='delete_node'),
    path('edit_node/<selected_id>', views.edit_node, name='edit_node'),
    path('change_colour/<selected_id>/<colour>', views.change_colour, name='change_colour'),
    path('mindmap', views.mindmap, name='mindmap'),
    path('mindmap/<id>', views.mindmap, name='mindmap'),
    path('mindmap/<id>/<selected_id>', views.mindmap, name='mindmap'),
    path('new', views.new, name='new'),
    path('new/<type>', views.new, name='new'),
    path('new/<type>/<parent_id>', views.new, name='new'),
    path('new/<type>/<parent_id>/<return_page>', views.new, name='new'),
    path('ind/<id>', views.ind, name='ind'),
    path('edit/<id>', views.edit, name='edit'),
    path('parent/<id>', views.parent, name='parent'),
    path('delete/<id>', views.delete, name='delete'),
    path('complete/<id>/<return_page>', views.complete, name='complete'),

    # path('', views.people_list, name='people_list'),

    path('people_list', views.people_list, name='people_list'),
    path('people_team/<id>', views.people_team, name='people_team'),
    path('people_ind/<id>', views.people_ind, name='people_ind'),
    path('people_skill_update/<people_id>/<sub_category_id>', views.people_skill_update, name='people_skill_update'),
    path('people_target_update/<people_id>/<sub_category_id>/<level_id>', views.people_target_update, name='people_target_update'),
    path('people_upload/<id>', views.people_upload, name='people_upload'),
    path('people_update/<id>', views.people_update, name='people_update'),
    path('people_delete/<id>', views.people_delete, name='people_delete'),
    path('people_delete_all', views.people_delete_all, name='people_delete_all'),

    path('skill_list', views.skill_list, name='skill_list'),
    path('level_list', views.level_list, name='level_list'),
    path('skill_ind/<sub_category_id>/<level_id>', views.skill_ind, name='skill_ind'),
    path('skill_cat_upload/<id>', views.skill_cat_upload, name='skill_cat_upload'),
    path('skill_upload/<id>', views.skill_upload, name='skill_upload'),
    path('level_upload/<id>', views.level_upload, name='level_upload'),
    path('role_upload/<id>', views.role_upload, name='role_upload'),
    path('skill_update/<id>', views.skill_update, name='skill_update'),
    path('skill_delete/<id>', views.skill_delete, name='skill_delete'),
    path('skill_delete_all', views.skill_delete_all, name='skill_delete_all'),
    path('level_delete_all', views.level_delete_all, name='level_delete_all'),
    path('role_delete_all', views.role_delete_all, name='role_delete_all'),

    path('colour_list', views.colour_list, name='colour_list'),
    path('colour_upload/<id>', views.colour_upload, name='colour_upload'),
    path('colour_activate/<id>', views.colour_activate, name='colour_activate'),
    path('colour_delete_all', views.colour_delete_all, name='colour_delete_all'),

    path('file_list', views.file_list, name='file_list'),
    path('file_upload', views.file_upload, name='file_upload'),
    path('file_delete/<file_id>', views.file_delete, name='file_delete'),
    # path('tinymce/', include(tinymce.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
