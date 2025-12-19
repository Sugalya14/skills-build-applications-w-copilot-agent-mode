from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentProfileViewSet)
router.register(r'teachers', views.TeacherProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'leaderboard', views.LeaderboardEntryViewSet)
router.register(r'suggestions', views.WorkoutSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
