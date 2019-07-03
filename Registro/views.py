from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
import json

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
        queryset = Asistencia.objects.filter(delete = False) #id.example2 = id.example
        #many = True, si aplica si se retorna varios objetos
        serializer = AsistenciaSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        v = False
        dato2= request.body
        datos=request.data["rfid"]
        diccionario={'rfid':datos}
        diccionario1 = {}
        serializer = AlumnoSerializers(data = diccionario)
        if serializer.is_valid():
            try:
                AlumnoData = Alumno.objects.get(rfid= diccionario['rfid'], delete = False)
                diccionario1 = {'id_Alumno':AlumnoData.id }
                try:
                    AsisData = Asistencia.objects.filter(fecha_hora = date.today())
                    for val in AsisData:
                        if val.id_Alumno.id == AlumnoData.id:
                            v = True
                    if v:
                        return Response("asistencia duplicada")
                    else:
                        serializer1 = AsistenciaSerializers(data = diccionario1)
                    if serializer1.is_valid():
                        serializer1.save()
                        return Response("Asistio el alumno")
                    else:
                        return Response("Fallo el registro del alumno")
                except Asistencia.DoesNotExist:
                    serializer1 = AsistenciaSerializers(data = diccionario1)
                    if serializer1.is_valid():
                        serializer1.save()
                        return Response("Asistio el alumno")
                    else:
                        return Response("Fallo el registro del alumno")
            except Alumno.DoesNotExist:
                if Alumno.objects.filter(rfid=diccionario['rfid']).exists():
                    return Response("Asistencia duplicada")
                else:

                    diccionario2 = {'rfid': datos,'name':'TestName2','matricula':'173221'}
                    serializer2 = AlumnoSerializers(data = diccionario2)
                if serializer2.is_valid():
                    serializer2.save()

                    diccionario99={'rfid':datos}
                    if Alumno.objects.filter(rfid=diccionario99['rfid']).exists():
                        AlumnoData2 = Alumno.objects.get(rfid=diccionario99['rfid'])
                        print(AlumnoData2.id)
                        diccionario999={'id_Alumno':AlumnoData2.id}
                        serializer11 = AsistenciaSerializers(data = diccionario999)
                    if serializer11.is_valid():
                        serializer11.save()
                        return Response("Asistio el alumno")
                        AlumnoData = null
                    else:
                        return Response("Fallo el registro del alumno")

                else:
                    return Response("Fallo la creacion del alumno")

            # return Response(datas)
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
