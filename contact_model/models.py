from django.db import models


class Contact(models.Model):
    contact = models.TextField()

    def __str__(self):
        return self.contact
