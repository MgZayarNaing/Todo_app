from email.policy import default
from django.db import models
from datetime import datetime
from my_app import enums
from django.utils import timezone
# Create your models here.

class TaskModel(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.task