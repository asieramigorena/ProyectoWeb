import csv
from django.core.management.base import BaseCommand
from ForoProyectos.models import Respuesta, Usuario, Pregunta
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):

    help = "Importa respuestas desde un CSV"

    def handle(self, *args, **kwargs):
        with open("ForoProyectos/resources/respuestas.csv", newline='', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            reader.fieldnames = [field.strip() for field in reader.fieldnames]

            for row in reader:
                row = {k.strip(): v.strip() for k, v in row.items()}

                autor_id = row.get("autor")
                pregunta_id = row.get("pregunta")
                contenido = row.get("contenido")
                fecha = row.get("fecha_publicacion")

                if not autor_id or not pregunta_id or not contenido:
                    self.stdout.write(self.style.WARNING("Fila incompleta, se omitirá"))
                    continue

                try:
                    autor = Usuario.objects.get(id=int(autor_id))
                except Usuario.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Usuario con id {autor_id} no existe. Se omite la fila."))
                    continue

                try:
                    pregunta = Pregunta.objects.get(id=int(pregunta_id))
                except Pregunta.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Pregunta con id {pregunta_id} no existe. Se omite la fila."))
                    continue

                respuesta_existente = Respuesta.objects.filter(
                    contenido=contenido,
                    autor=autor,
                    pregunta=pregunta
                ).first()

                if respuesta_existente:
                    self.stdout.write(self.style.WARNING(f"Respuesta ya existe: {contenido[:30]}..."))
                    continue

                Respuesta.objects.create(
                    contenido=contenido,
                    autor=autor,
                    pregunta=pregunta,
                    fecha_publicacion=parse_datetime(fecha) if fecha else None
                )

                self.stdout.write(self.style.SUCCESS(f"Respuesta importada para pregunta id {pregunta.id}"))
