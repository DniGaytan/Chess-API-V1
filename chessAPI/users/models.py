from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default = 1, primary_key = True)
    birthdate = models.DateField()
    picture_link = models.URLField(max_length=255)

    class Meta:
        db_table = "user_extra"

