from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    USER_TYPE = [
        ('admin','admin'),
        ('member','member')
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    
    

