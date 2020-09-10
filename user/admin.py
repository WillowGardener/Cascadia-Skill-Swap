from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
from .forms import UserProfileCreationForm, UserProfileChangeForm

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['hometown','username','profile_pic','experiences','teach_skills','learn_skills','forum_posts']

admin.site.register(UserProfile)

