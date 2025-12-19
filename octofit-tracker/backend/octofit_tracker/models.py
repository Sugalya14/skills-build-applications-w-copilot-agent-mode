from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=32, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Student: {self.user.get_username()}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    school = models.CharField(max_length=128, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Teacher: {self.user.get_username()}"


class Team(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(StudentProfile, related_name='teams', blank=True)
    created_by = models.ForeignKey(TeacherProfile, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Activity(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=64)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.get_username()} - {self.activity_type} @ {self.timestamp}"


class LeaderboardEntry(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.student.user.get_username()} : {self.score}"


class WorkoutSuggestion(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='suggestions')
    title = models.CharField(max_length=128)
    description = models.TextField()
    difficulty = models.CharField(max_length=32, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion for {self.student.user.get_username()}: {self.title}"
