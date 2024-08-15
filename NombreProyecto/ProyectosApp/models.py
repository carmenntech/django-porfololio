from django.db import models

# Create your models here.

class Proyectos (models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    descripcion_proyecto = models.CharField(max_length=5000)
    fecha_creacion= models.DateTimeField()
    imagen = models.ImageField(upload_to='proyectos')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre_proyecto

