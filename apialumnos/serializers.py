from rest_framework import serializers
from .models import Alumno, Profesor, Usuario, Archivo, ArchivoHistorial


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre',
                  'apellido',
                  'telefono',
                  'mail',
                  'fecha_creacion',
                  'fecha_alta')
