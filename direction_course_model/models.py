from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.direction} {self.name}"
