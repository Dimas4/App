from django.db import models

from direction_course_model.models import Direction
from test_student_model.models import Lesson, Work
from homework_model.models import HomeWork
from like_model.models import Like


class Course(models.Model):
    training = models.BooleanField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    banner = models.ImageField(blank=True, null=True)
    upcoming_webinar = models.DateTimeField(blank=True, null=True)
    progress = models.IntegerField()
    leave_course = models.BooleanField()
    price = models.IntegerField()
    student_count = models.PositiveIntegerField(blank=True, null=True, default=0)

    home_work = models.ManyToManyField(HomeWork, blank=True)
    lesson = models.ManyToManyField(Lesson, blank=True)
    work = models.ManyToManyField(Work, blank=True)
    likes = models.ManyToManyField(Like, blank=True)

    def __str__(self):
        return self.name
