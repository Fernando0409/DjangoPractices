from django.db import models
from django.db.models import TextField


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = TextField(blank=True)

