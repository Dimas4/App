from django.db import models


class HomeWork(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
