from django.db import models


class Message(models.Model):
    profile_id = models.IntegerField()
    text = models.TextField()

    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile_id} {self.text[:10]}"
