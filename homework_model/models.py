from django.db import models


class HomeWork(models.Model):
    text = models.TextField()
    lesson_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.text} {self.lesson_id}"
