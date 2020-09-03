from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    hometown = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="media/")

class Experience(models.Model):
    organization = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    dates = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class TeachSkill(models.Model):
    skill_category = models.TextField()
    skill_description = models.CharField(max_length=50)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class LearnSkill(models.Model):
    skill_category = models.TextField()
    skill_description = models.CharField(max_length=50)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class ForumPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_body = models.TextField()
    post_timestamp = models.DateTimeField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    

