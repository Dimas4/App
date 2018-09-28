from django.db import models


class Comment(models.Model):
    course_id = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.course_id} {self.text[:10]}"
