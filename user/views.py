from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserProfileCreationForm
from .models import UserProfile
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class CreateProfile(CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('user_profile.html')
    template_name = 'create_profile.html'
    
    
class SignUpView(CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class OtherUserDetail(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'
    permission_classes = [IsOwnerOrReadOnly]

class OtherUserListView(ListView):
    model = UserProfile
    template_name = 'search.html'
    permission_classes = [IsOwnerOrReadOnly]
