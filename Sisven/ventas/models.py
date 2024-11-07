from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=59,verbose_name='Nombre: ',unique= True,blank=False,help_text='ingresa solo texto')

def _str_(self):
    return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre: ',unique= True,blank=False)
    precio = models.DecimalField(max_digits=4,decimal_places=2,verbose_name='Precio',blank=False)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

def _str_(self):
    return self.nombre

class CLiente(models.Model):
    cedula = models.CharField(max_length=10,verbose_name='Cedula :',unique=True,blank=False,null=False)
    nombre = models.CharField(max_length=50,verbose_name='Cliente :',blank=False)
    apellido = models.CharField(max_length=50,verbose_name='Cliente :',blank=False)
    edad = models.IntegerField()
    correo = models.EmailField()
    domicilio = models.TextField(max_length=200,help_text='Esribe la referencia de tu domicilio')

def _str_(self):
    return f'{self.nombre}{self.apellido}'

class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=4,decimal_places=2)
    CLiente = models.ForeignKey(CLiente, on_delete=models.RESTRICT)
    Producto = models.ManyToManyField(Producto)

def _str_(self):
    return f'Orden de{self.id} - Cliente: {self.cliente.nombre}'