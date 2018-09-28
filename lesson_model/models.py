from django.db import models


class Lesson(models.Model):
    description = models.TextField()
    course_id = models.IntegerField()

    def __str__(self):
        return self.description
