from django.shortcuts import render
from ContenidoApp.models import  Post, Categoria

# Create your views here.
def contenido(request):

   
    Post_list = Post.objects.all()

    return render ( request , 'contenido/contenido.html', {'Post_list':Post_list} )

#tenemos que pasarle categoria id 
def categoria(request, categoria_id):

    #almacenamos la categoria que nos pasan por id
    categoria_get = Categoria.objects.get(id=categoria_id)
    #filtramos los post por esa categoria 
    Post_list = Post.objects.filter(categoria = categoria_get)
    return render ( request , 'contenido/categoria.html', {'categoria_get':categoria_get, 'Post_list':Post_list} )
