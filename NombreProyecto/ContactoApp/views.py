from django.shortcuts import redirect, render, HttpResponse
from .forms import FormularioContacto



# Create your views here.
def contacto(request):

    formulario = FormularioContacto()

    if request.method == 'POST':
        formulario = FormularioContacto(data = request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('Nombre')
            email = request.POST.get('Email')
            contenido = request.POST.get('Contenido')
            redirect_contacto = redirect('/contacto/?valido')
            return redirect_contacto

    return render(request,'contacto/contacto.html', {'formulario': formulario})

