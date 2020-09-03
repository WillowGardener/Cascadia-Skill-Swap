from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from user import models

class NestedExperienceSerializer(serializer.ModelSerializer):
    class Meta:
        model = Experience 
        fields = ['organization','role','dates','description','author']


class NestedLearnSkillsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Skill 
        fields = ['skill_category','skill_description','author']

class NestedTeachSkillsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Skill 
        fields = ['skill_category','skill_description','author']

class NestedForumPostsSerializer(serializer.ModelSerializer):
    model = ForumPost 
    fields = ['post_title','post_body','post_timestamp','author']

class UserProfileSerializer(serializers.ModelSerializer):
    experiences = NestedExperienceSerializer(read_only=True, many=True)
    teach_skills = NestedTeachSkillsSerializer(read_only=True, many=True)
    learn_skills = NestedLearnSkillsSerializer(read_only=True, many=True)
    forum_posts = NestedForumPostsSerializer(read_only=True, many=True)
    class Meta:        
        model = models.UserProfile
        fields = ['id','hometown','profile_pic','experiences','teach_skills','learn_skills','forum_posts']