# subjects/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=200)  # Teacher's name and surname

    def __str__(self):
        return self.title
