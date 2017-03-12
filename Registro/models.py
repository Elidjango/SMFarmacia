#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class pacientes(models.Model):
	cedula = models.CharField(max_length=10, null=True, blank=True, unique=True)
	nombre_paci = models.CharField(max_length=50, null=True)
	apellido_paci = models.CharField(max_length=50, null=True)
	cod_movil = models.IntegerField()
	movil = models.IntegerField()
	cod_tlf = models.IntegerField()
	tlf = models.IntegerField()
	direccion_paci = models.TextField(max_length=255, null=True)
	fech_naci = models.DateField(null=True)
	tiempo_registro_paciente = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado_paciente = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		Dato ="%s %s %s"% (self.cedula, self.nombre_paci, self.apellido_paci)
		return Dato

class medicamentos(models.Model):
	codigo_med = models.CharField(max_length=10, null=True)
	nombre_med = models.CharField(max_length=50, null=True)
	numero_lote = models.CharField(max_length=20, null=True)
	fecha_elavorado = models.DateField(null=True)
	fecha_vencimiento = models.DateField(null=True)
	tipo = models.CharField(max_length=50, null=True)
	cantidad = models.IntegerField(null=True)
	precio = models.IntegerField(null=True)
	tiempo_registro_medicamentos = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado_medicamentos = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		Dato2 ="%s %s"% (self.codigo_med, self.nombre_med)
		return Dato2

class servicios(models.Model):
	codigo_serv = models.IntegerField(null=True)
	nombre_serv = models.CharField(max_length=50, null=True)
	tipo2 = models.CharField(max_length=50, null=True)
	extencion_tlf = models.IntegerField(null=True)
	asistente_serv = models.CharField(max_length=50, null=True)
	tiempo_registro_servicios = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado_servicios = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		Dato3 ="%i %s"% (self.codigo_serv, self.nombre_serv)
		return Dato3		