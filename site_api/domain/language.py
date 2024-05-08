from django.db import models

class Language(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    name = models.CharField(max_length=50)
    startDateUse = models.DateField()
    level = models.CharField(
        max_length=1,
        choices=NIVEL,
        blank=False,
        null=False,
        default='B')

    def __str__(self) -> str:
        return self.name