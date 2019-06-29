from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from Registro.models import Alumno
from Registro.models import Asistencia

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('__all__')

        ################