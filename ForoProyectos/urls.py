from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('usuario/', views.UsuarioListView.as_view(), name='lista_usuarios'),
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(), name='detalle_usuario'),

    path('pregunta/', views.PreguntaListView.as_view(), name='lista_preguntas'),
    path('pregunta/<int:pk>', views.PreguntaDetailView.as_view(), name='detalle_preguntas'),

    path('respuesta/', views.RespuestaListView.as_view(), name='lista_respuestas'),
    path('respuesta/<int:pk>', views.RespuestaDetailView.as_view(), name='detalle_respuestas'),
]
