from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.contenido, name ='Contenido' ),
    #pasamos el id de la categoria por parametro
    path('categoria/<int:categoria_id>', views.categoria, name ='Categoria'),

    #path('categoria', views.categoria, name ='Categoria'),
    
   
]