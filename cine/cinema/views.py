from django.shortcuts import render, redirect
from .models import Pelicula, Comentario, Sesion, Asiento, Reserva
import datetime
from django.core import serializers

from django.utils import timezone
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
asientosActualizados = []


def index(request):

	peliculas = []
	sesiones = Sesion.objects.all()
	for i in sesiones:
		print (i.hora)
		if i.hora > timezone.now():
			if i.pelicula not in peliculas:
				peliculas.append(i.pelicula)
	generos = []
	peliculas_g = Pelicula.objects.all()
	generos = []
	for i in peliculas_g:
		print (i.genero)

		if i.genero not in generos:
			generos.append(i.genero)

	return render(request, 'cinema/index.html', {'peliculas': peliculas, 'generos': generos});

def filtrogenero(request):

	sesiones = Sesion.objects.all()

	peliculas_g = Pelicula.objects.all()
	generos = []
	for i in peliculas_g:
		print (i.genero)

		if i.genero not in generos:
			generos.append(i.genero)
	peliculas = []
	for i in sesiones:
		print (i.hora)
		if i.hora > timezone.now() and i.pelicula.genero == request.GET["genero"]:
			if i.pelicula not in peliculas:
				peliculas.append(i.pelicula)
#	peliculas = Pelicula.objects.filter(genero=request.GET["genero"])
	
	return render(request, 'cinema/index.html', {'peliculas': peliculas, 'generos': generos})


def detalle(request, id):
    try:
        pelicula = Pelicula.objects.get(pk=id)
    except:
        raise Http404('La pelicula no existe')
    comentarios = Comentario.objects.filter(pelicula = pelicula)
    sesiones = Sesion.objects.filter(pelicula = pelicula)
    ss = [];
    for i in sesiones:
    	if i.hora > timezone.now():
    		ss.append(i)
    return render(request, 'cinema/detallePelicula.html', {'pelicula': pelicula, 'comentarios':comentarios, 'sesiones':ss})

def reserva(request,id):
	asientosActualizados = []
	try:
		pelicula = Pelicula.objects.get(pk=id)
		sesiones = Sesion.objects.filter(pelicula = pelicula)
        #filtar por fecha
	except:
		raise Http404('La pelicula no existe')

	return render(request, 'cinema/reserva.html', {'sesiones': sesiones, 'pelicula':pelicula})

def guardarReserva(request):
	reservaTxt = request.POST["sesionesSeleccionadas"]
	#reservaTxt = "$2_1$1_4"
	reservas = []
	aux = []
	for i in range(0, len(reservaTxt)):
		if reservaTxt[i] == '$':
			if len(aux) != 0:
				reservas.append(aux)
				aux = []
		elif reservaTxt[i] != '_':
			aux.append(int(reservaTxt[i]))

	reservas.append(aux)
	sesiones = []
	sesion = Sesion.objects.get(pk=reservas[0][0])
	print( asientosActualizados)
	for i in reservas:
		sesion = Sesion.objects.get(pk=i[0])
		r = Reserva.objects.create(sesion= sesion, nEntradas= i[1])
		sesiones.append(r)

	return render(request, 'cinema/guardarReserva.html', {'reservas': sesiones, 'pelicula':sesion.pelicula});
	
def volver(request):
	return render(request, 'cinema/index.html');

def reservaList(request):
	
	peliculas = []
	sesiones = Sesion.objects.all()
	for i in sesiones:
		print (i.hora)
		if i.hora > timezone.now():
			if i.pelicula not in peliculas:
				peliculas.append(i.pelicula)
	return render(request, 'cinema/reservaList.html', {'peliculas': peliculas});

def comentar(request):
	nombre=request.POST["nombre"]
	contenido=request.POST["comentario"]
	id=request.POST["id"]
	pelicula=Pelicula.objects.get(id=request.POST["id"])
	fecha = datetime.datetime.now()

	comentario = Comentario.objects.create(pelicula=pelicula, nombre=nombre,fecha=fecha, contenido=contenido)
	return redirect('detalle/'+id)

def buscar(request):
	texto=request.GET["filtroBusqueda"]
	print(texto)
	p_titulo = Pelicula.objects.filter(titulo=texto)
	p_dir = Pelicula.objects.filter(director=texto)
	peliculas = []
	for i in p_titulo:
		peliculas.append(i)
	for i in p_dir:
		peliculas.append(i)

	return render(request, 'cinema/resultadosBusqueda.html', {'peliculas': peliculas});

def asientos(request, id):
	sesion = Sesion.objects.get(pk=id)
	res = Asiento.objects.filter(sesion=sesion)
	asientos = serializers.serialize('json',res)
	return HttpResponse(asientos, content_type="application/json")

def ocuparAsiento(request, id, asientos):
	sesion = Sesion.objects.get(pk=id)
	asientosActuales = Asiento.objects.filter(sesion=sesion)

	for i in range(0, len(asientos)):
		print(asientosActuales[i].libre, asientos[i])
		if(asientosActuales[i].libre != int(asientos[i])):
			print ('Entro')
			asiento = asientosActuales[i]
			asiento.libre = int(asientos[i])
			asientosActualizados.append(asiento)
			asiento.save()
	return HttpResponse()