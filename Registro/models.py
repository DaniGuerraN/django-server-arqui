from django.db import models
from django.utils import timezone

class RFID(models.Model):
    id_Asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    rfid = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.rfid

    class Meta:
        db_table = 'Rfid'

class Asistencia(models.Model):
    name = models.CharField(max_length=254, null=False)
    matricula = models.IntegerField(max_value= 9,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'
