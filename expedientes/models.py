from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Archivo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='archivos/%Y/%m/%d/')
    nombre_original = models.CharField(max_length=255, blank=True)
    subido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_original or self.archivo.name
