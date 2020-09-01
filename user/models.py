from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    hometown = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="media/")

    #for user's resume
    resume_organization = models.CharField(max_length=50)
    resume_role = models.CharField(max_length=50)
    resume_dates = models.CharField(max_length=50)
    resume_description = models.TextField

    #for user's desired skills and skills to teach
    skill_category = models.TextField
    skill_description = models.CharField(max_length=50)

    #list of user's forum posts
    post_title = models.CharField(max_length=50)
    post_body = models.TextField
    post_timestamp = models.DateTimeField


    

