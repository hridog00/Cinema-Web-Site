from django.urls import  path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:id_pelicula', views.detalle, name='detalle'),
    path('reserva/<int:id_pelicula', views.reserva, name='reserva'),
    path('guardarReserva', views.guardarReserva, name='guardarReserva'),
	path('volver', views.volver, name='volver'),
  #  path('formulario-opciones/<int:id_encuesta>', views.formulario_opciones, name='formulario-opciones'),
  #  path('vota', views.vota, name='vota'),
  #  path('resultados/<int:id_encuesta>', views.resultados, name='resultados'),
   # path('ajax/', views.llamadaAjax, name='ajax'),
   # path('pagina-ajax/', views.paginaAjax, name='fajax'),
]
