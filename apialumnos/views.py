from rest_framework import viewsets

from .serializers import AlumnoSerializer
from .models import Alumno


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer