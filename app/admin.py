from django.contrib import admin

from .models import People, Skill, File
admin.site.register(People)
admin.site.register(Skill)
admin.site.register(File)
