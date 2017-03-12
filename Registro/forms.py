#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class PaciForm(forms.ModelForm):

	css_error_class = 'has-error'
	
	class Meta:
		model = pacientes

		fields = ('cedula', 'nombre_paci', 'apellido_paci', 'cod_movil', 'movil',
			'cod_tlf', 'tlf', 'direccion_paci', 'fech_naci')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})

class MediForm(forms.ModelForm):
	
	css_error_class = 'has-error'
	
	class Meta:
		model = medicamentos

		fields = ('codigo_med', 'nombre_med', 'numero_lote', 'fecha_elavorado', 'fecha_vencimiento',
			'tipo', 'cantidad', 'precio')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})

class ServiForm(forms.ModelForm):
	
	css_error_class = 'has-error'
	
	class Meta:
		model = servicios

		fields = ('codigo_serv', 'nombre_serv', 'tipo2', 'extencion_tlf', 'asistente_serv')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs.update({'class':'form-control'})