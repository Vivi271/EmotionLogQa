from django.db import models

class EmotionEntry(models.Model):
    user = models.CharField(max_length=100)        # Campo para almacenar el nombre del usuario
    emotion_level = models.IntegerField()          # Campo para almacenar el nivel de emoción
    date = models.DateTimeField(auto_now_add=True) # Campo para almacenar la fecha y hora del registro, con valor predeterminado de la fecha y hora actual
    emotion_type = models.CharField(max_length=50) # Campo para almacenar el tipo de emoción (feliz, triste, enojado, etc.)
    description = models.TextField(null=True, blank=True)  # Campo opcional para que el usuario pueda agregar una descripción
    location = models.CharField(max_length=100, null=True, blank=True)  # Campo opcional para almacenar la ubicación
    activity = models.CharField(max_length=100, null=True, blank=True)  # Campo opcional para almacenar la actividad que realizaba el usuario

