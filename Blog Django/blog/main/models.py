from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    contenido = models.TextField(max_length=1500, null=True)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.FileField(blank=True, null=True, upload_to="opinion")
    usuario_crea = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
