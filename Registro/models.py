from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    name = models.CharField(max_length=254, null=False)
    matricula = models.IntegerField(null=False)
    rfid = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Alumno'


class Asistencia(models.Model):
    id_Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id_Alumno

    class Meta:
        db_table = 'Asistencia'
