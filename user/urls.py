from django.urls import path
from .views import CreateProfile, SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    
    path('create_profile/', CreateProfile.as_view(), name='create'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name = 'user_profile.html')),
    path('search/', TemplateView.as_view(template_name='search.html')),
    path('search/api/v1', TemplateView.as_view(template_name='search.html'))
]