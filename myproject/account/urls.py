from django.urls import path
from .views import *

urlpatterns = [
    path('signUpPage/',signUpPage,name='signUpPage'),
    path('',loginPage,name='loginPage'),
    path('logoutPage',logoutPage,name='logoutPage'),
    path('homePage/',homePage,name='homePage'),
    path('profilePage/',profilePage,name='profilePage'),
    path('editProfilePage/',editProfilePage,name='editProfilePage'),
]
