"""SMfarmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout
from reportes.views import ReportePacientesPDF, ReporteMedicamentosPDF
from Registro import views
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    #------------------------FRONT INICIAL------------------------------------------------------#
    url(r'^$', login, {'template_name': 'index.html', }, name="login_index"),
    url(r'^mision/$', 'home.views.mision', name='Mision'),
    url(r'^vision/$', 'home.views.vision', name='Vision'),
    url(r'^quienes_somos/$', 'home.views.quienes_somos', name='Quienes_Somos'),
    #-------------------------------------------------------------------------------------------#
    

    #------------------------PRELOADER----------------------------------------------------------#
    url(r'^preloader/$', 'home.views.preloader', name='preloader'),
    #-------------------------------------------------------------------------------------------#
    

    #------------------------FRONT SECUNDARIO---------------------------------------------------#
    url(r'^home/$', 'home.views.home', name='home'),
    url(r'^logout/$', logout, {'template_name': 'logout.html', }, name="logout"),
    url(r'^signup/$', 'home.views.signup', name='signup'),
    url(r'^signup/success/$', 'home.views.register_success', name="success_signup"),
    #-------------------------------------------------------------------------------------------#


    #-------------------------PACIENTES---------------------------------------------------------#
    url(r'^pacientes/$', 'Registro.views.paciente', name="rg_pacientes"),
    #-------------------------------------------------------------------------------------------#


    #-------------------------MEDICAMENTOS------------------------------------------------------#
    url(r'^medicamentos/$', 'Registro.views.medicamento'),
        url(r'^mtr_medicamentos/$', 'Registro.views.mostrar_medicamentos', name="mostrar_medicamentos"), 
        url(r'^medicinas_habiles/$', 'Registro.views.mostrar_medi_index', name="mostrar_medicamentos_index"),
        url(r'^medicamentos/(?P<pk>\d+)/editar/$', views.UpdateMediView.as_view(), name='editar_medicamentos'),
        url(r'^medicamentos/(?P<pk>\d+)/eliminar/$', views.eliminar_medicamentos, name='eliminar_medicamentos'),  
    #-------------------------------------------------------------------------------------------#


    #-------------------------SERVICIOS---------------------------------------------------------#
    #-------------------------------------------------------------------------------------------#


    #-------------------------MANUAL DE USUARIOS------------------------------------------------#
    url(r'^ayuda/$', 'reportes.views.ayuda'),
    #-------------------------------------------------------------------------------------------#


    #-------------------------REPORTE IMPORTANTE------------------------------------------------#
    url(r'^reporte_pacientes_pdf/$',login_required(ReportePacientesPDF.as_view())),
    url(r'^reporte_medicamentos_pdf/$',login_required(ReporteMedicamentosPDF.as_view())),
    url(r'^change_views/', 'reportes.views.pdf_view'),
    #-------------------------------------------------------------------------------------------#
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
