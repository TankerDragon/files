from statistics import mode
from django.db import models

# Create your models here.
class Log(models.Model):
    data = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    is_overloaded = models.BooleanField(default=False)