from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('usuario/<int:pk>', views.detalle_usuario, name='detalle_usuario')
]
