from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    mail = models.EmailField()
    password = models.CharField(max_length=60)
    fecha_creacion = models.DateField()
    fecha_alta = models.DateField()
    fecha_baja = models.DateField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["fecha_creacion"]
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


class Alumno(Usuario):
    legajo = models.IntegerField()

    class Meta:
        ordering = ["legajo"]
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"


class Profesor(Usuario):

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"


class Archivo(models.Model):
    url = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=60)
    fecha_subida = models.DateField()
    estado = models.CharField(max_length=60)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ["fecha_subida"]
        verbose_name = "archivo"
        verbose_name_plural = "archivos"


class ArchivoHistorial(models.Model):
    fecha = models.DateField()
    nuevo_estado = models.CharField(max_length=60)
    archivo_id = models.ForeignKey(Archivo, on_delete=models.DO_NOTHING)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nuevo_estado

    class Meta:
        ordering = ["fecha"]
