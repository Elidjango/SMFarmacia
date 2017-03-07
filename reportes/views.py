#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import BytesIO
from reportlab.pdfgen import canvas
#pip install reportlab
from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response, redirect
from reportlab.lib.utils import ImageReader


#probando algo nuevo
from django.conf import settings
from io import BytesIO
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.pagesizes import A4, cm, letter
from reportlab.lib import colors
#finnnnnn

from reportes.models import *
from Registro.models import pacientes, medicamentos

from django.contrib.auth.decorators import login_required

@login_required()
def ayuda(request):
    return render_to_response('ayuda.html')

class ReportePacientesPDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/img/paci.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, -50, 750, 420, 90,preserveAspectRatio=True)

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Cedúla', 'Nombre', 'Apellido', 'Codigo', 'Movil', 'Dirección', 'Fecha/NCMT')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(xd.cedula, xd.nombre_paci, xd.apellido_paci, xd.cod_movil, xd.movil, xd.direccion_paci, xd.fech_naci) for xd in pacientes.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm,
         3 * cm, 2 * cm, 3 * cm, 4 * cm, 3 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 520)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 15,y)                   
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "Reportes_pacientes.pdf"
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 520
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteMedicamentosPDF(View):  
     
    """def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/img/.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, -50, 750, 420, 90,preserveAspectRatio=True)"""

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Codigo', 'Nombre del Medicamento', 'N° Lote', 'Elavorado', 'Vence', 'Cantidad')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(xd.codigo_med, xd.nombre_med, xd.numero_lote, xd.fecha_elavorado, xd.fecha_vencimiento, xd.cantidad) for xd in medicamentos.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 8 * cm,
         2 * cm, 3 * cm, 3 * cm, 2 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 750)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 15,y)                   
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "Reportes_medicamentos.pdf"
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        y = 750
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

def pdf_view(request):
    with open(r'C:\\Users\\Anonymous\\Documents\\SISTEMAS\\system\\original\\media\\documents\\SOLICITUD.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        pdf_name = "Pantilla_Necesaria.pdf"
        return response    