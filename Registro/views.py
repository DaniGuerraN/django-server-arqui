from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Registro.models import Alumno
from Registro.models import Asistencia

from Registro.serializer import AlumnoSerializers
from Registro.serializer import AsistenciaSerializers

class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete = False)  #id.example2 = id.example
        #many = True, si aplica si se retorna varios objetos
        serializer = AlumnoSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data

            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnoDetail(APIView):
    def get_object(self, id):
        try: 
            return Alumno.objects.get(pk= id, delete = False)
        except Alumno.DoesNoExist:
            return 404
    
    def get(self, request, id, format= None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(rfid, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else: 
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

####################################################################################
class AsistenciaList(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects.filter(delete = False)  #id.example2 = id.example
        #many = True, si aplica si se retorna varios objetos
        serializer = AsistenciaSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data

            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AsistenciaDetail(APIView):
    def get_object(self, id):
        try: 
            return Asistencia.objects.get(pk= id, delete = False)
        except Asistencia.DoesNoExist:
            return 404
    
    def get(self, request, id,format= None):
        asistencia = self.get_object(id)
        if asistencia != 404:
            serializer = AsistenciaSerializers(asistencia)
            return Response(serializer.data)
        else:
            return Response(asistencia, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        asistencia = self.get_object(id)
        if asistencia != 404:
            serializer = AsistenciaSerializers(asistencia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else: 
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
