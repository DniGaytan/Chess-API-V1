from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 1, primary_key=True)
    username = models.CharField(max_length=100)
    elo_score = models.IntegerField()
    picture_link = models.URLField(max_length=255)
