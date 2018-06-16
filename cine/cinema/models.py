from django.db import models

# Create your models here.
class Pelicula(models.Model):
	titulo = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	genero = models.CharField(max_length=50)
	sinopsis = models.CharField(max_length=600)
	foto = models.ImageField()

class Sala(models.Model):
	numeroSala = models.IntegerField()
	numeroFilas = models.IntegerField()
	nAsientosFila = models.IntegerField()
	nAsientosUltimaFila = models.IntegerField()

class Sesion(models.Model):
	hora = models.DateTimeField();
	pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
	sala = models.ForeignKey(Sala, on_delete = models.CASCADE)


class Comentario(models.Model):
	pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
	fecha = models.DateField();
	nombre = models.CharField(max_length=50)
	contenido = models.CharField(max_length=300)

class Asiento(models.Model):
	fila = models.IntegerField()
	numero = models.IntegerField()
	sesion = models.ForeignKey(Sesion, on_delete = models.CASCADE)
	libre = models.IntegerField(default=0)

class Reserva(models.Model):
	nEntradas = models.IntegerField()
	sesion = models.ForeignKey(Sesion, on_delete = models.CASCADE)
