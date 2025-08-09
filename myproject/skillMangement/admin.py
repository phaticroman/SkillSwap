from django.contrib import admin
from .models import SkillModel,Comment,UserSkill,UserWantToLearn

admin.site.register(SkillModel)
admin.site.register(Comment)
admin.site.register(UserSkill)
admin.site.register(UserWantToLearn)
