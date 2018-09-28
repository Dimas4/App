from django.db import models


class Like(models.Model):
    profile_id = models.IntegerField()

    def __str__(self):
        return f"{self.profile_id}"
