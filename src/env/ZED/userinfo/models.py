from django.db import models
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.username
