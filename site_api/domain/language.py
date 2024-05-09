from django.db import models
import uuid

class Language(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=50)
    start_date_use = models.DateField()
    level = models.CharField(
        max_length=1,
        choices=NIVEL,
        default='B')

    def __str__(self) -> str:
        return self.name