from rest_framework import serializers
from . import models


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentProfile
        fields = ['id', 'user', 'age', 'grade', 'bio']


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherProfile
        fields = ['id', 'user', 'school', 'bio']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ['id', 'student', 'activity_type', 'duration_minutes', 'distance_km', 'calories', 'timestamp']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'name', 'members', 'created_by']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeaderboardEntry
        fields = ['id', 'student', 'score', 'updated_at']


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkoutSuggestion
        fields = ['id', 'student', 'title', 'description', 'difficulty', 'created_at']
