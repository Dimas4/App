from django.db import models


class Contact(models.Model):
    name = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.contact
