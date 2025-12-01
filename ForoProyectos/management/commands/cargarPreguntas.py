import csv
from django.core.management.base import BaseCommand
from ForoProyectos.models import Pregunta, Usuario

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open("ForoProyectos/resources/preguntas.csv", newline='', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            
            reader.fieldnames = [field.strip() for field in reader.fieldnames]

            for row in reader:
                row = {k.strip(): v.strip() for k, v in row.items()}

                autor_id = row.get("autor")
                autor, created = Usuario.objects.get_or_create(
                    id=int(autor_id),
                    defaults={
                        "username": f"usuario{autor_id}",
                        "email": f"usuario{autor_id}@example.com",
                        "contraseña": "123456",
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Usuario creado: {autor.username}"))

                pregunta_existente = Pregunta.objects.filter(
                    titulo=row["titulo"],
                    autor=autor
                ).first()

                if pregunta_existente:
                    self.stdout.write(self.style.WARNING(f"Pregunta ya existe: {row['titulo']}"))
                    continue

                Pregunta.objects.create(
                    titulo=row["titulo"],
                    contenido=row["contenido"],
                    autor=autor
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Pregunta importada: {row['titulo']}")
                )