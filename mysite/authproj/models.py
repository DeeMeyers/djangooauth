from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):
    current = models.IntegerField(blank=True, null=True)
    previous = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(blank=True, null=True)
    currentLogin = models.DateTimeField(auto_now_add= True)
    lastLogin = models.DateTimeField(blank=True, null=True)
