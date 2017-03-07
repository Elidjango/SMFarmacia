from django.contrib import admin

from .models import *
# Register your models here.

class AdminPacientes(admin.ModelAdmin):
	list_display = ['__str__','cod_movil','movil','cod_tlf','tlf','direccion_paci',
	'fech_naci','tiempo_registro_paciente','actualizado_paciente']
	class Meta:
		model = pacientes
admin.site.register(pacientes, AdminPacientes)

class AdminMedicamentos(admin.ModelAdmin):
	list_display = ['__str__','numero_lote','fecha_elavorado',
	'fecha_vencimiento','tipo','cantidad','precio','tiempo_registro_medicamentos',
	'actualizado_medicamentos']
	class Meta:
		model = medicamentos
admin.site.register(medicamentos, AdminMedicamentos)

class AdminServicios(admin.ModelAdmin):
	list_display = ['__str__','tipo','extencion_tlf','asistente_serv',
	'tiempo_registro_servicios','actualizado_servicios']
	class Meta:
		model = servicios
admin.site.register(servicios, AdminServicios)