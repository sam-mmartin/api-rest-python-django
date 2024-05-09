from django.db import models
from .social import Social
from .language import Language
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    work = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language,
                                       through='UserLanguage')
    socials_medias = models.ManyToManyField(Social,
                                            through='UserSocialMedia')

    def __str__(self) -> str:
        return self.name
