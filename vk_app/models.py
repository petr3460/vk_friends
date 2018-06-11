from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    vk_id = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
