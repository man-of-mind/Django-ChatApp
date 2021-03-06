from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)



class Message(models.Model):
    message  = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=200)
    room = models.CharField(max_length=200)