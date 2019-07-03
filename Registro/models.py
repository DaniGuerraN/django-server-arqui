from django.db import models
from django.utils import timezone
import datetime

class Alumno(models.Model):
    name = models.CharField(max_length=254, null=True)
    matricula = models.IntegerField(null=True)
    rfid = models.CharField(max_length=254, null=True)
    delete = models.BooleanField(default=True)
    create = models.DateTimeField(default=timezone.now)
    fecha_hora = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Alumno'


class Asistencia(models.Model):
    id_Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    fecha_hora = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.id_Alumno

    class Meta:
        db_table = 'Asistencia'
