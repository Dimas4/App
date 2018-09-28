from django.db import models

from test_student_model.models import Lesson
from homework_model.models import HomeWork
from comments_model.models import Comment
from message_model.models import Message
from contact_model.models import Contact
from course_model.models import Course


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    email = models.EmailField()

    contact = models.ManyToManyField(Contact, blank=True)
    course = models.ManyToManyField(Course, blank=True)
    my_homework = models.ManyToManyField(HomeWork, blank=True)
    saved_lesson = models.ManyToManyField(Lesson, blank=True)
    message = models.ManyToManyField(Message, blank=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
