
from operator import mod
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.conf import settings


class Club(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=9,null=True)
   
    def __str__(self) :
        return  self.nombre

opciones_consultas =[
    ['consulta', "consulta"],
    ["reclamo","reclamo"],
    ["sugerencia","sugerencia"],
    ["felicitaciones","felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.CharField(choices=opciones_consultas,null=True,max_length=20)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def get_absolute_url(self):
       
        return reverse('contacto-detail', args=[str(self.id)])
    
    def __str__(self) :
        return self.nombre

class Pistas(models.Model):
    club=models.ForeignKey(Club, on_delete=models.CASCADE,null=True)
    nombre=models.CharField(max_length=50)
    numero=models.IntegerField()
    codigo=models.CharField(max_length=50)
    imagen= models.ImageField(upload_to="pistas", null=True , blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('pista-detail', args=[str(self.id)])
    
    def __str__(self) :
        return  self.nombre
       
class Hora(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE,null=True)
    hora=models.CharField(null=True,max_length=20)
    def __str__(self) :
        return  self.hora

opciones_hora =[
    ["17:00","17:00"],
    ["18:30","18:30"],
    ["20:00","20:00"],
    ["21:30","21:30"]
]
class Reservas(models.Model):
    nombre=models.CharField(max_length=50,null=True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    club=models.ForeignKey(Club,on_delete=models.CASCADE,null=True) 
    pista= models.ForeignKey(Pistas, on_delete=models.CASCADE)
    fecha=models.DateField()
    hora=models.ForeignKey(Hora,on_delete=models.CASCADE,null=True)
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('reserva-detail', args=[str(self.id)])


    def __str__(self) :
        return  self.nombre


# hora=models.CharField(choices=opciones_hora,null=True,max_length=20)