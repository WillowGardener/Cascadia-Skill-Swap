from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExperienceViewSet, LearnSkillViewSet,TeachSkillViewSet,ForumPostViewSet, UserProfileList, UserProfileDetail, UserProfileViewSet


router = DefaultRouter()

# router.register('userprofiles', UserProfileViewSet, basename='userprofiles')
router.register('experiences', ExperienceViewSet, basename="experiences")
router.register('learnskills', LearnSkillViewSet, basename="learnskills")
router.register('teachskills', TeachSkillViewSet, basename="teachskills")
router.register('forumposts', ForumPostViewSet, basename="forumpost")
router.register('userprofiles', UserProfileViewSet, basename="userprofile")

urlpatterns = router.urls
urlpatterns = [
    path('',include(router.urls)),
    path('user/', UserProfileList.as_view()),
    path('user-profile/', UserProfileDetail.as_view())
]