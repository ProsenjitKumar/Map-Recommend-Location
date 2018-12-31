from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='accounts/', blank=None)
    bio = models.TextField()
    birth_date = models.DateField()
    friends = models.IntegerField()
    following = models.IntegerField()
    follower = models.IntegerField()


    def __str__(self):
        return self.user
