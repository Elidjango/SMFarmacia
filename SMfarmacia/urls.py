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
    #sistema de autenticacion login
    url(r'^$', login, {'template_name': 'index.html', }, name="login"),
    url(r'^logout/$', logout, {'template_name': 'logout.html', }),
    #cambiar el usuario y la contraseña
    url(r'^signup/$', 'home.views.signup', name='signup'),
    url(r'^signup/success/$', 'home.views.register_success'),
    #inicio del sistema
    url(r'^preloader/$', 'home.views.preloader', name='preloader'),
    #url(r'^uploads/', 'reportes.views.upload_file', name="uploads"),

    url(r'^mision/$', 'home.views.mision', name='home'),
    url(r'^vision/$', 'home.views.vision', name='home'),
    url(r'^quienes_somos/$', 'home.views.quienes_somos', name='home'),

    url(r'^home/$', 'home.views.home', name='home'),

    url(r'^pacientes/$', 'Registro.views.paciente'),
        url(r'^mtr_pacientes/$', 'Registro.views.mostrar_pacientes'),
        #url(r'^pacientes/(?P<pk>\d+)/editar/$',editarPaciUpdate.as_view(),name='editar'),
        url(r'^pacientes/(?P<pk>\d+)/editar/$', views.UpdatePaciView.as_view(), name='editar_pacientes'),

    url(r'^medicamentos/$', 'Registro.views.medicamento'),
        url(r'^mtr_medicamentos/$', 'Registro.views.mostrar_medicamentos', name="mostrar_medicamentos"), 
        url(r'^medicinas_habiles/$', 'Registro.views.mostrar_medi_index', name="mostrar_medicamentos_index"),
        url(r'^medicamentos/(?P<pk>\d+)/editar/$', views.UpdateMediView.as_view(), name='editar_medicamentos'),
        url(r'^medicamentos/(?P<pk>\d+)/eliminar/$', views.eliminar_medicamentos, name='eliminar_medicamentos'),

    url(r'^servicios/$', 'Registro.views.servicio'),    

    #REPORTE IMPORTANTE APARTE
    url(r'^ayuda/$', 'reportes.views.ayuda'),

    url(r'^reporte_pacientes_pdf/$',login_required(ReportePacientesPDF.as_view())),
    url(r'^reporte_medicamentos_pdf/$',login_required(ReporteMedicamentosPDF.as_view())),

    url(r'^change_views/', 'reportes.views.pdf_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
