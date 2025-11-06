from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),

    path('usuario/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:pk>', views.detalle_usuario, name='detalle_usuario'),

    path('pregunta/', views.lista_preguntas, name='lista_preguntas'),
    path('pregunta/<int:pk>', views.detalle_preguntas, name='detalle_preguntas'),

    path('respuesta/', views.lista_respuestas, name='lista_respuestas'),
    path('respuesta/<int:pk>', views.detalle_respuestas, name='detalle_respuestas')
]
