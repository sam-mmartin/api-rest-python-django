from django.db import models
from .user import User
from .social import Social
from .language import Language

class UserSocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)

class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)