from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=11)
