from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser,MemberProfile
from django.http import HttpResponse
from skillMangement.models import UserSkill,UserWantToLearn



def signUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        if not all ([username,email,password]):
            return HttpResponse("Please fill all fields")
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        user = CustomUser.objects.create_user(username=username,email=email,password=password,last_name=last_name,first_name=first_name,user_type=user_type)
        if user.user_type == 'member':
            MemberProfile.objects.create(user=user)
        user.save()
        return redirect('loginPage')
    return render(request,'registration/signUpPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'registration/loginPage.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def homePage(request):
    return render(request,'common/base.html')


def profilePage(request):
    current_user = request.user
    profile = get_object_or_404(MemberProfile,user=current_user)
    user_skills = UserSkill.objects.filter(user=current_user)
    user_want_skill = UserWantToLearn.objects.filter(user = current_user)
    return render(request,'UserInfo/profilePage.html',{'profile':profile,'user_skills':user_skills,'user_want_skill':user_want_skill})

        
def editProfilePage(request):
    current_user = request.user
    memberprofile, created = MemberProfile.objects.get_or_create(user=current_user)

    if request.method == 'POST':
        if request.user:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            bio = request.POST.get('bio')
            profile_picture = request.FILES.get('profile_picture')

            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.save()


            memberprofile.bio = bio
            if profile_picture:
                memberprofile.profile_picture = profile_picture
            memberprofile.save()

        return redirect('profilePage')

    context = {
        'user': current_user,
        'memberprofile': memberprofile,
    }
    return render(request, 'UserInfo/editProfilePage.html', context)
