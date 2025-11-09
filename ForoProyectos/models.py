from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    foto = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username

class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=2000)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="preguntas")
    foto = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    contenido = models.TextField(max_length=2000)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="respuestas_autor")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="respuestas")
    foto = models.URLField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return f"Respuesta de {self.autor} a {self.pregunta}"
