from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria (models.Model):
    nombre_categoria = models.CharField(max_length=200)
    descripcion_categoria = models.CharField(max_length=5000)
    fecha_creacion_post= models.DateTimeField()
    #created= models.DateTimeField(auto_now_add=True)
    #updeted= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre_categoria
    

class Post (models.Model):
    titulo_post = models.CharField(max_length=200)
    contenido_post = models.CharField(max_length=5000)
    fecha_creacion_post= models.DateTimeField()
    #relacion entre tablas, para que si se elimina un usuario se eliminen los post asociados
    autor_post = models.ForeignKey(User, on_delete = models.CASCADE) 
    #relacion varios a varios 
    categoria = models.ManyToManyField(Categoria)
    #nul = true para decir que no es necesario ese registro
    imagen = models.ImageField(upload_to='contenido', null=True, blank=True)

    #created= models.DateTimeField(auto_now_add=True)
    #updeted= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo_post
    

