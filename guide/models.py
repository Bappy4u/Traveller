from django.db import models
from django.contrib.auth.models import User


class GuideProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    is_guide = models.BooleanField(default=False)
    love = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar',blank=True)

