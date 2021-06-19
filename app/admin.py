from django.contrib import admin

from .models import People, Skill, Skill_Cat, Skill_Level, Score, Target, File
admin.site.register(People)
admin.site.register(Skill_Cat)
admin.site.register(Skill_Level)
admin.site.register(Skill)
admin.site.register(Score)
admin.site.register(Target)
admin.site.register(File)
