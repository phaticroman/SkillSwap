from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from account.models import CustomUser,MemberProfile
from django.http import HttpResponse
from .models import *

def createSkill(request):
    user = request.user
    if request.method == 'POST':
        skill = SkillModel.objects.create(skill_name=request.POST.get('skill_name'),duration=request.POST.get('duration'),description=request.POST.get('description'),skil_pic=request.FILES.get('skil_pic'),user=request.user)
        skill.save()
        return redirect('skillList')
    return render(request,'skill/create_skill.html')

def skillList(request):
    skills = SkillModel.objects.all()
    return render(request,'skill/skill_list.html',{'skills':skills})

def skillDetails(request,id):
    skill = get_object_or_404(SkillModel,id=id)
    comments = Comment.objects.filter(skill=skill).order_by('-created_at')
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(skill=skill, user=request.user, text=text)
            return redirect('skillDetail', id=skill.id)
    return render(request,'skill/skill_detail.html',{'skill':skill,'comments': comments})

def skillWanted(request):
    if request.method == 'POST':
        wanted_skill = UserWantToLearn.objects.create(
            user=request.user,
            skill_name=request.POST.get('skill_name'),
        )
        return redirect('profilePage')
    return render(request,'skill/skillWanted.html')


def matchskill(request):
    user = request.user
    user_skills = UserSkill.objects.filter(user=user).values_list('user_skill_name',flat=True)
    skil_match = SkillModel.objects.filter(skill_name__in = user_skills)
    return render(request,'skill/match_skill.html',{'skil_match':skil_match})
    
def PostUserPorfile(request,id):
    user = get_object_or_404(CustomUser,id=id)
    profile = MemberProfile.objects.get(user=user)
    user_skills = UserSkill.objects.filter(user=user)
    user_want_skill = UserWantToLearn.objects.filter(user = user)
    return render(request,'skill/user_profile.html',{ 'user': user,
        'profile': profile,
        'user_skills': user_skills,
        'user_want_skills': user_want_skill})