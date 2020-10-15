from django.contrib import admin
from .models import Alumno, Profesor, Usuario, Archivo, ArchivoHistorial


# Register your models here.
admin.site.register(Alumno)
admin.site.register(Archivo)
admin.site.register(ArchivoHistorial)
admin.site.register(Profesor)
admin.site.register(Usuario)
