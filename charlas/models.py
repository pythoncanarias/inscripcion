# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Charla(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre



class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nif = models.CharField(verbose_name="Número de documento (NIF)", max_length=9, blank=True, null=True, help_text="Necesitamos "
        "el número de su DNI para pasarlo a la empresa de seguridad (obligatorio)")
    usuario_ull = models.CharField(verbose_name="Usuario ULL", max_length=100, blank=True, null=True, help_text="Escriba su "
        "nombre de usuario de la ULL, si dispone de el, por ser alumno o pas o pdi")
    ects = models.BooleanField(verbose_name="¿Solicita ECTS?", default=False, help_text="Marque la casilla si quiere "
        "que se le convalide los cursos por créditos ECTS")
    email = models.EmailField(verbose_name="Correo electrónico", max_length=100, help_text="Se le enviará un correo "
        "electrónico para la confirmación de esta dirección, y otro correo cuando haya que "
        "confirmar la reserva, además de otras informaciones de última hora relacionadas con "
        "el curso (obligatorio)")
    curriculum = models.FileField(verbose_name="Currículum Vitae", upload_to="cvs", blank=True, null=True, help_text="Si quiere "
        "que demos su currículum se ceda a las empresas patrocinadoras")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    charla = models.ForeignKey(Charla, verbose_name="Estilo de charla elegida", help_text="Charla a la que desea asistir")
