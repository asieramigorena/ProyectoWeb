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
