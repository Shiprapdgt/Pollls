from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return  self.key
