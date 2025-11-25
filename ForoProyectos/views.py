from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Pregunta, Respuesta
from django.views.generic import ListView, DetailView, TemplateView

class IndexView(TemplateView):
    template_name = "index.html"


# --- Usuarios ---
class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"
    context_object_name = "usuarios"


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuario/detalle_usuario.html"
    context_object_name = "usuario"


# --- Preguntas ---
class PreguntaListView(ListView):
    model = Pregunta
    template_name = "pregunta/lista_preguntas.html"
    context_object_name = "preguntas"


class PreguntaDetailView(DetailView):
    model = Pregunta
    template_name = "pregunta/detalle_preguntas.html"
    context_object_name = "pregunta"


# --- Respuestas ---
class RespuestaListView(ListView):
    model = Respuesta
    template_name = "respuesta/lista_respuestas.html"
    context_object_name = "respuestas"


class RespuestaDetailView(DetailView):
    model = Respuesta
    template_name = "respuesta/detalle_respuestas.html"
    context_object_name = "respuesta"
