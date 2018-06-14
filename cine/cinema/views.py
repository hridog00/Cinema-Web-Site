from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'cinema/index.html');

def detalle(request, id_pelicula):
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
    except:
        raise Http404('La pelicula no existe')
    return render(request, 'pelicula/detalle.html', {'pelicula': pelicula})

def reserva(request, id_pelicula):
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
    except:
        raise Http404('La pelicula no existe')
    return render(request, 'pelicula/reserva.html', {'pelicula': pelicula})

def guardarReserva(request):
	return render(request, 'cinema/guardarReserva.html');
	
def volver(request):
	return render(request, 'cinema/index.html');
