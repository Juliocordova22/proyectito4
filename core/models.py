from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre
    

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre



class Ordentrabajo(models.Model):
    ot = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    id_ascensor = models.CharField(max_length=20)
    modelo_ascensor = models.CharField(max_length=25)
    fallas_detectadas = models.TextField(null=True,blank=True)
    reparacion_efectuada = models.TextField(null=True,blank=True)
    piezas_cambiadas = models.TextField(null=True,blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ascensor
        
  




