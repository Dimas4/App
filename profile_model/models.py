from django.db import models

from homework_model.models import HomeWork
from contact_model.models import Contact
from course_model.models import Course
from lesson_model.models import Lesson


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    avatar = models.ImageField()
    about_me = models.TextField()

    contacts = models.ManyToManyField(Contact)
    course = models.ManyToManyField(Course)
    my_homework = models.ManyToManyField(HomeWork)
    saved_lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
