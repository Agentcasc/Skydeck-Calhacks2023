from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    teacherID = models.CharField(max_length=10, default="0000000000")
    extracurriculars = models.TextField(blank=True)
    introverted_extroverted = models.CharField(max_length=20, blank=True)
    interests = models.TextField(blank=True)
    who_you_are = models.TextField(blank=True)
    county_in_california = models.CharField(max_length=30, blank=True)
    future_career_aspirations = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    num_classrooms = models.IntegerField(default=0)
    num_students = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class classroom(models.Model):
    id = models.AutoField(primary_key=True)
    teacherID = models.CharField(max_length=10, default="0000000000")
    name = models.CharField(max_length=30, default="Classroom")
    num_students = models.IntegerField(default=0)
    students = models.TextField(blank=True)
    teacher = models.TextField(blank=True)
    def __str__(self):
        return self.name
