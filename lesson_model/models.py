from django.db import models


class Lesson(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
