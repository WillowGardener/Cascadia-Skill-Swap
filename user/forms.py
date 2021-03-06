from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username','email', 'hometown', 'profile_pic']

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = UserChangeForm.Meta.fields