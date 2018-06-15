from django.urls import  path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
    path('reservaList', views.reservaList, name='reservaList'),
    path('catalogo', views.index, name='catalogo'),
    path('filtrogenero', views.filtrogenero, name='filtrogenero'),
    path('comentar', views.comentar, name='comentar'),
    path('reserva/asientosSesion/<int:id>', views.asientos, name='asientosSesion'),
    path('reserva/<int:id>', views.reserva, name='reserva'),
    path('guardarReserva', views.guardarReserva, name='guardarReserva'),
	path('volver', views.volver, name='volver'),
	path('buscar', views.buscar, name='buscar'),

  #  path('formulario-opciones/<int:id_encuesta>', views.formulario_opciones, name='formulario-opciones'),
  #  path('vota', views.vota, name='vota'),
  #  path('resultados/<int:id_encuesta>', views.resultados, name='resultados'),
   # path('ajax/', views.llamadaAjax, name='ajax'),
   # path('pagina-ajax/', views.paginaAjax, name='fajax'),
]
