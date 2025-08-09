from django.db import models
from account.models import CustomUser,MemberProfile

class SkillModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100,null=True)
    description = models.TextField()
    skil_pic = models.ImageField(upload_to='skill_pics',blank=True,null=True)
    
    def save(self,*args, **kwargs):
        skill_name_normalized = self.skill_name.strip().lower()
        self.skill_name = skill_name_normalized
        user_skill = UserSkill.objects.filter(user_skill_name=skill_name_normalized,user=self.user)
        if not user_skill.exists():
            UserSkill.objects.create(user_skill_name=skill_name_normalized,user=self.user)
        super().save(*args, **kwargs)
            
    
    def __str__(self):
        return f'{self.skill_name} Created By {self.user.last_name}'

class Comment(models.Model):
    skill = models.ForeignKey(SkillModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'comment By {self.user.last_name} on {self.skill.skill_name}'


class UserSkill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_skill_name = models.CharField(max_length=100)
    class Meta:
        unique_together =('user','user_skill_name')
    
    def __str__(self):
        return f"{self.user.username} - {self.user_skill_name}"


class UserWantToLearn(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        skill_name_normalized = self.skill_name.strip().lower()
        self.skill_name = skill_name_normalized
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.username} Want To Learn {self.skill_name}'