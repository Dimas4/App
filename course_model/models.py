from django.db import models

from direction_course_model.models import Direction
from test_student_model.models import Lesson, Test
from homework_model.models import HomeWork
from like_model.models import Like


class Course(models.Model):
    training = models.BooleanField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    banner = models.ImageField()
    upcoming_webinar = models.DateTimeField()
    progress = models.IntegerField()
    leave_course = models.BooleanField()
    price = models.IntegerField()
    student_count = models.PositiveIntegerField()

    direction = models.ManyToManyField(Direction)
    home_work = models.ManyToManyField(HomeWork)
    lesson = models.ManyToManyField(Lesson)
    test = models.ManyToManyField(Test)
    likes = models.ManyToManyField(Like)

    def __str__(self):
        return self.name
