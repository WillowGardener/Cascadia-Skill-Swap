from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from user import models

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Author
#         fields = ['author']

class NestedUserProfileSerializer(serializers.ModelSerializer):
    class Meta:        
        model = models.UserProfile
        fields = ['id', 'username', 'profile_pic']

class ExperienceSerializer(serializers.ModelSerializer):
    username = NestedUserProfileSerializer(read_only=True, source = 'author')
    class Meta:
        model = models.Experience
        fields = ['organization','role','dates','description', 'author','username']

class NestedExperienceSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True, many=True)
    class Meta:
        model = models.Experience 
        fields = ['organization','role','dates','description']

class LearnSkillSerializer(serializers.ModelSerializer):
    username = NestedUserProfileSerializer(read_only=True, many=True, source = 'user_profile')
    class Meta:
        model = models.LearnSkill 
        fields = ['skill_category','skill_description', 'user_profile', 'username']

class TeachSkillSerializer(serializers.ModelSerializer):
    username = NestedUserProfileSerializer(read_only=True, many=True, source = 'user_profile')
    class Meta:
        model = models.TeachSkill 
        fields = ['skill_category','skill_description', 'user_profile','username']

class NestedLearnSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LearnSkill 
        fields = ['skill_category','skill_description']

class NestedTeachSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeachSkill 
        fields = ['skill_category','skill_description',]

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumPost 
        fields = ['post_title','post_body','post_timestamp','author']        

class NestedForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumPost 
        fields = ['post_title','post_body','post_timestamp']

class UserProfileSerializer(serializers.ModelSerializer):
    experiences = NestedExperienceSerializer(read_only=True, many=True, source = 'experience_set')
    teach_skills = NestedTeachSkillSerializer(read_only=True, many=True, source = 'teachskill_set')
    learn_skills = NestedLearnSkillSerializer(read_only=True, many=True, source = 'learnskill_set')
    forum_posts = NestedForumPostSerializer(read_only=True, many=True)
    class Meta:        
        model = models.UserProfile
        fields = ['id', 'username','email','hometown','profile_pic','experiences','teach_skills','learn_skills','forum_posts','experience_set', 'teachskill_set', 'learnskill_set']


