from django.shortcuts import render

from rest_framework import viewsets, generics, filters

from user.models import UserProfile, Experience, TeachSkill, LearnSkill, ForumPost
from .serializers import UserProfileSerializer, ExperienceSerializer, TeachSkillSerializer, LearnSkillSerializer, ForumPostSerializer



# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hometown']
    def get_object(self):
        print(self.request.user)
        return self.request.user
    

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['organization','role','description']

class TeachSkillViewSet(viewsets.ModelViewSet):
    queryset = TeachSkill.objects.all()
    serializer_class = TeachSkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['skill_category','skill_description']

class LearnSkillViewSet (viewsets.ModelViewSet):
    queryset = LearnSkill.objects.all()
    serializer_class = LearnSkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['skill_category','skill_description']

class ForumPostViewSet (viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class UserProfileViewSet (viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hometown']
