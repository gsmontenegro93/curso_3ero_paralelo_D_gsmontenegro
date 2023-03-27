from django.db import models

# Create your models here.
class curso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-"
        return texto.format(self.id, self.nombre, self.direccion, self.telefono)

    class Meta: db_table = 'duenomascota'


class estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    materia = models.TextField()
    estado = models.BooleanField(default=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-"
        return texto.format(self.id, self.nombre, self.materia, self.estado)

    class Meta: db_table = 'animal'