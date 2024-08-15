from django.shortcuts import render
from ProyectosApp.models import Proyectos

# Create your views here.
def proyectos(request):

    #cargamos todos los proyectos
    Proyectos_list = Proyectos.objects.all()

    return render ( request , 'proyectos/proyectos.html' , {'Proyectos_list': Proyectos_list } )
