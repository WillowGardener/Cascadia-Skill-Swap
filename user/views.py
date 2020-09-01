from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserProfileCreationForm

class CreateProfile(CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('user_profile.html')
    template_name = 'create_profile.html'
    
