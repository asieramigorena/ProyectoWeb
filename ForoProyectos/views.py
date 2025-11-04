from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    context = {'usuario': usuario}
    return render(request, 'usuario/detalle_usuario.html', context)
