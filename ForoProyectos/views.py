from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Pregunta, Respuesta

# Create your views here.
def index(request):
    return render(request, "index.html")

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    context = {'usuario': usuario}
    return render(request, 'usuario/detalle_usuario.html', context)

def lista_preguntas(request):
    preguntas =Pregunta.objects.all()
    return render(request, 'pregunta/lista_preguntas.html', {'preguntas': preguntas})

def detalle_preguntas(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)
    context = {'pregunta': pregunta}
    return render(request, 'pregunta/detalle_preguntas.html', context)

def lista_respuestas(request):
    respuestas = Respuesta.objects.all()
    return render(request, 'respuesta/lista_respuestas.html', {'respuestas': respuestas})

def detalle_respuestas(request, pk):
    respuestas = get_object_or_404(Respuesta, pk=pk)
    context = {'respuesta': respuestas}
    return render(request, 'respuesta/detalle_respuestas.html', context)
