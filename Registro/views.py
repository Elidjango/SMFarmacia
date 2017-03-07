#!/usr/bin/python
# -*- coding: utf-8 -*-
#_______________________________________
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
#________________________________________
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import ListView 
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.db.models import Q
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

from .models import *
from .forms import *
# Create your views here.

@login_required()
def paciente(request):
	form = PaciForm(request.GET or None)

	Context={

	"form":form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		cedula = form_data.get("cedula")
		nombre_paci = form_data.get("nombre_paci")
		apellido_paci = form_data.get("apellido_paci")
		cod_movil = form_data.get("cod_movil")
		movil = form_data.get("movil")
		cod_tlf = form_data.get("cod_tlf")
		tlf = form_data.get("tlf")
		direccion_paci = form_data.get("direccion_paci")
		fech_naci = form_data.get("fech_naci")

		obj = pacientes.objects.create(cedula=cedula, nombre_paci=nombre_paci,
			apellido_paci=apellido_paci, cod_movil=cod_movil, movil=movil, 
			cod_tlf=cod_tlf, tlf=tlf,
			direccion_paci=direccion_paci, fech_naci=fech_naci)
	else:
		print ("No Existe")

	return render(request,"rg_pacientes.html",Context)

@login_required()
def mostrar_pacientes(request):
	queryset_list = pacientes.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
			queryset_list = queryset_list.filter(
				Q(cedula__icontains=query)|
				Q(nombre_paci__icontains=query)|
				Q(apellido_paci__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 50)
	Page_reques_var = "page"
	page = request.GET.get(Page_reques_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	
	contexto = {
	'object_list':queryset,
	'cedula': 'List',
	'nombre_paci':'List',
	'apellido_paci' : 'List',
	'cod_movil': 'List',
	'movil': 'List',
	'cod_tlf': 'List',
	'tlf': 'List',
	'direccion_paci': 'List',
	'fech_naci': 'List',
	'Page_reques_var': Page_reques_var
	}
	return render(request, 'mtr_pacientes.html', contexto)

class UpdatePaciView(UpdateView):
	"""Vista para editar eventos."""

	model = pacientes
	template_name = 'edit_pacientes.html'
	form_class = PaciForm
	success_url = reverse_lazy('mostrar_pacientes', args=(0, ))

	def form_valid(self, form):
		pacientes = form.instance
		self.success_url = reverse_lazy('mostrar_pacientes', args=(pacientes.pk, ))
		return super().form_valid(form)		

#####################################################################################
######################################################################################
######################################################################################

@login_required()
def medicamento(request):
	form = MediForm(request.GET or None)

	Context={

	"form":form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		codigo = form_data.get("codigo")
		nombre_med = form_data.get("nombre_med")
		numero_lote = form_data.get("numero_lote")
		fecha_elavorado = form_data.get("fecha_elavorado")
		fecha_vencimiento = form_data.get("fecha_vencimiento")
		tipo = form_data.get("tipo")
		cantidad = form_data.get("cantidad")
		precio = form_data.get("precio")

		obj = medicamentos.objects.create(codigo=codigo, nombre_med=nombre_med,
			numero_lote=numero_lote, fecha_elavorado=fecha_elavorado, fecha_vencimiento=fecha_vencimiento, 
			tipo=tipo, cantidad=cantidad,precio=precio)
	else:
		print ("No Existe")

	return render(request,"rg_medicamentos.html",Context)

@login_required()
def mostrar_medicamentos(request):
	queryset_list = medicamentos.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
			queryset_list = queryset_list.filter(
				Q(codigo__icontains=query)|
				Q(nombre_med__icontains=query)|
				Q(numero_lote__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 50)
	Page_reques_var = "page"
	page = request.GET.get(Page_reques_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	
	contexto = {
	'object_list':queryset,
	'codigo': 'List',
	'nombre_med':'List',
	'numero_lote' : 'List',
	'fecha_elavorado': 'List',
	'fecha_vencimiento': 'List',
	'tipo': 'List',
	'cantidad': 'List',
	#'precio': 'List',
	'Page_reques_var': Page_reques_var
	}
	return render(request, 'mtr_medicamentos.html', contexto)

def mostrar_medi_index(request):
	queryset_list = medicamentos.objects.all()
	Page_reques_var = "page"
	query = request.GET.get("q")
	if query:
			queryset_list = queryset_list.filter(
				Q(codigo__icontains=query)|
				Q(nombre_med__icontains=query)|
				Q(numero_lote__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 50)
	Page_reques_var = "page"
	page = request.GET.get(Page_reques_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	
	contexto = {
	'object_list':queryset,
	'codigo': 'List',
	'nombre_med':'List',
	'numero_lote' : 'List',
	'fecha_elavorado': 'List',
	'fecha_vencimiento': 'List',
	'tipo': 'List',
	'cantidad': 'List',
	#'precio': 'List',
	'Page_reques_var': Page_reques_var
	}
	return render(request, 'mtr_med_index.html', contexto)

class UpdateMediView(UpdateView):
	"""Vista para editar eventos."""

	model = medicamentos
	template_name = 'edit_medicamentos.html'
	form_class = MediForm
	success_url = reverse_lazy('mostrar_medicamentos', args=(0, ))

	def form_valid(self, form):
		medicamentos = form.instance
		self.success_url = reverse_lazy('mostrar_medicamentos', args=(medicamentos.pk, ))
		return super().form_valid(form)	

def eliminar_medicamentos(request, pk):
	"""Vista para eliminar los eventos."""

	medi = get_object_or_404(medicamentos, pk=pk)
	medi.delete()
	return redirect('mostrar_medicamentos')

######################################################################################
######################################################################################
######################################################################################	

@login_required()
def servicio(request):
	form = ServForm(request.POST or None)

	Context={

	"form":form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		codigo = form_data.get("codigo")
		nombre_serv = form_data.get("nombre_serv")
		tipo = form_data.get("tipo")
		extencion_tlf = form_data.get("extencion_tlf")
		asistente_serv = form_data.get("asistente_serv")

		obj = servicios.objects.create(codigo=codigo, nombre_serv=nombre_serv,
			tipo=tipo, extencion_tlf=extencion_tlf, asistente_serv=asistente_serv)
	else:
		print ("No Existe")

	return render(request,"rg_servicios.html",Context)