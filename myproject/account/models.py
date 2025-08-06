from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    USER_TYPE = [
        ('admin','admin'),
        ('member','member')
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=50)
    email = models.EmailField(max_length=255, unique=True,null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
    
class MemberProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f'Name : {self.user.username}'
    
    
    
    

