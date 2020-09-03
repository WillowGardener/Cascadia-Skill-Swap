from django.shortcuts import render

from rest_framework import viewsets

from user.models import UserProfile, Experience, TeachSkill, LearnSkill, ForumPost
from .serializers import UserProfileSerializer, ExperienceSerializer, TeachSkillSerializer, LearnSkillSerializer, ForumPostSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class TeachSkillViewSet(viewsets.ModelViewSet):
    queryset = TeachSkill.objects.all()
    serializer_class = TeachSkillSerializer

class LearnSkillViewSet (viewsets.ModelViewSet):
    queryset = LearnSkill.objects.all()
    serializer_class = LearnSkillSerializer

class ForumPostViewSet (viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

