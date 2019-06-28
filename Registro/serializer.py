from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from Registro.models import RFID
from Registro.models import Asistencia

class RFIDSerializers(serializers.ModelSerializer):
    class Meta:
        model = RFID
        fields = ('__all__')

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('__all__')

        ################