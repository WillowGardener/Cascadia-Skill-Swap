from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, ExperienceViewSet, LearnSkillViewSet,TeachSkillViewSet,ForumPostViewSet


router = DefaultRouter()

router.register('userprofiles', UserProfileViewSet, basename='userprofiles')
router.register('experiences', ExperienceViewSet, basename="experiences")
router.register('learnskills', LearnSkillViewSet, basename="learnskills")
router.register('teachskills', TeachSkillViewSet, basename="teachskills")
router.register('forumposts', ForumPostViewSet, basename="forumpost")

urlpatterns = router.urls
urlpatterns = [
    path('',include(router.urls))
]