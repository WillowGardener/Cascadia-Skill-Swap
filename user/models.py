from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    hometown = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="media/")
    class Meta:
        verbose_name = 'User_Profile'
    

class Experience(models.Model):
    organization = models.CharField(max_length=50)
    role = models.CharField(max_length=50,null=True,blank=True)
    dates = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Experience'
    

class TeachSkill(models.Model):
    skill_category = models.TextField()
    skill_description = models.CharField(max_length=50)
    user_profile = models.ManyToManyField(UserProfile, verbose_name = "User_Profile")
    class Meta:
        verbose_name = 'Teach_Skill'
    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class LearnSkill(models.Model):
    skill_category = models.TextField()
    skill_description = models.CharField(max_length=50)
    user_profile = models.ManyToManyField(UserProfile, verbose_name = "User_Profile")
    class Meta:
        verbose_name = 'Learn_Skill'
    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class ForumPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_body = models.TextField()
    post_timestamp = models.DateTimeField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Forum_Post'
    


    
    


    

