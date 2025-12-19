from django.contrib import admin
from . import models


@admin.register(models.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'grade')


@admin.register(models.TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('student', 'activity_type', 'duration_minutes', 'timestamp')


@admin.register(models.LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'updated_at')


@admin.register(models.WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'difficulty', 'created_at')
