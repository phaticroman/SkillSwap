from django.contrib import admin
from .models import CustomUser,MemberProfile

admin.site.register(CustomUser)
admin.site.register(MemberProfile)