from django.db import models
from .user import User

class Social(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}/{self.username}'
