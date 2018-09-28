from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    course_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.direction} {self.name}"
