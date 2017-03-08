#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.contrib.auth.models import User

class PaciForm(forms.ModelForm):
	
	class Meta:
		model = pacientes
			
		fields = [
			'cedula',
			'nombre_paci',
			'apellido_paci',
			'cod_movil',
			'movil',
			'cod_tlf',
			'tlf',
			'direccion_paci',
			'fech_naci',
		]
		widgets = {
		 	'cedula': forms.NumberInput(attrs={'class':'form-control'}),
		 	'nombre_paci': forms.TextInput(attrs={'class': 'form-control'}),
		 	'apellido_paci': forms.TextInput(attrs={'class': 'form-control'}),
		 	'cod_movil': forms.NumberInput(attrs={'class': 'form-control'}),
		 	'movil': forms.NumberInput(attrs={'class': 'form-control'}),
		 	'cod_tlf': forms.NumberInput(attrs={'class': 'form-control'}),
		 	'tlf': forms.NumberInput(attrs={'class': 'form-control'}),
		 	'direccion_paci': forms.TextInput(attrs={'class': 'form-control' }),
		 	'fech_naci': forms.DateInput(attrs={'class': 'form-control'}),
		}

class MediForm(forms.ModelForm):
	
	class Meta:
		model = medicamentos
			
		fields = [
			'codigo_med',
			'nombre_med',
			'numero_lote',
			'fecha_elavorado',
			'fecha_vencimiento',
			'tipo',
			'cantidad',
			'precio',
		]
		widgets = {
		 	'codigo_med': forms.TextInput(attrs={'class':'form-control'}),
		 	'nombre_med': forms.TextInput(attrs={'class': 'form-control'}),
		 	'numero_lote': forms.TextInput(attrs={'class': 'form-control'}),
		 	'fecha_elavorado': forms.TextInput(attrs={'class': 'form-control'}),
		 	'fecha_vencimiento': forms.TextInput(attrs={'class': 'form-control'}),
		 	'tipo': forms.TextInput(attrs={'class': 'form-control' }),
		 	'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
		 	'precio': forms.NumberInput(attrs={'class': 'form-control'}),
		}