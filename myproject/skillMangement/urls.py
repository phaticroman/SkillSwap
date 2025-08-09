from django.urls import path
from .views import *

urlpatterns = [
    path('createSkill/',createSkill,name='createSkill'),
    path('skillList/',skillList,name='skillList'),
    path('skillDetail/<int:id>',skillDetails,name='skillDetail'),
    path('skillWanted',skillWanted,name='skillWanted'),
    path('matchskill',matchskill,name='matchskill'),
    path('PostUserPorfile<int:id>',PostUserPorfile,name='PostUserPorfile'),
]
