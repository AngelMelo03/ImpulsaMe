from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [('docente', 'Docente'), ('estudiante', 'Estudiante')]
    AREA_CHOICES = [('salud', 'Salud'), ('cultura', 'Cultura'), ('ciencia', 'Ciencia')]

    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    area_ensenanza = models.CharField(max_length=10, choices=AREA_CHOICES, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
