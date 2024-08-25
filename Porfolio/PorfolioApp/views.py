from django.shortcuts import render, HttpResponse




# Create your views here.
def inicio(request):
    return render(request,'PorfolioApp/inicio.html')

