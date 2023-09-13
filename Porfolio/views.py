from django.shortcuts import render
from .models import Proyecto

def home(request):
    return render(request, 'home.html')

def Project(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'Proyectos/proyectos.html', {'proyectos':proyectos})

