from django.db import models


class Note(models.Model):
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.note