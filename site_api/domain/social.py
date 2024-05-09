from django.db import models
import uuid

class Social(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}/{self.username}'
