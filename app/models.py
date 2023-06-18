from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


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

    # Additional fields for job description preferences
    work_indoors = models.BooleanField(default=False)
    work_outdoors = models.BooleanField(default=False)
    fast_paced_environment = models.BooleanField(default=False)
    relaxed_environment = models.BooleanField(default=False)
    collaborative_team = models.BooleanField(default=False)
    independent_work = models.BooleanField(default=False)
    physically_demanding_work = models.BooleanField(default=False)
    willing_to_travel = models.BooleanField(default=False)
    flexible_work_hours = models.BooleanField(default=False)
    structured_environment = models.BooleanField(default=False)
    casual_environment = models.BooleanField(default=False)
    competitive_atmosphere = models.BooleanField(default=False)
    supportive_atmosphere = models.BooleanField(default=False)
    job_variety = models.BooleanField(default=False)
    routine_oriented = models.BooleanField(default=False)
    customer_interaction = models.BooleanField(default=False)
    work_life_balance = models.BooleanField(default=False)
    comfortable_with_technology = models.BooleanField(default=False)
    open_to_learning = models.BooleanField(default=False)

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
