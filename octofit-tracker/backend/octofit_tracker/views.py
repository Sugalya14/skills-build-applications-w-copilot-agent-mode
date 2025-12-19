from rest_framework import viewsets, permissions
from . import models, serializers


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = models.StudentProfile.objects.all()
    serializer_class = serializers.StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = models.TeacherProfile.objects.all()
    serializer_class = serializers.TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = models.LeaderboardEntry.objects.all()
    serializer_class = serializers.LeaderboardEntrySerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = models.WorkoutSuggestion.objects.all()
    serializer_class = serializers.WorkoutSuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]
