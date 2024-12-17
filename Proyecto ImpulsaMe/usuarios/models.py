from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [('docente', 'Docente'), ('estudiante', 'Estudiante')]
    AREA_CHOICES = [('salud', 'Salud'), ('cultura', 'Cultura'), ('ciencia', 'Ciencia')]

    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    area_ensenanza = models.CharField(max_length=10, choices=AREA_CHOICES, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.content[:30]}"
