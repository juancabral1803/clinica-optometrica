from django.db import models

# Create your models here.
class Hero(models.Model):
    # id is auto generated primary key
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    # add auto_now_add to set birthday to creation date
    birthday = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name

class paciente(models.Model):
    nombre_apellido = models.CharField(max_length=80)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre_apellido


class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=20)
    rol = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_usuario    




class medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.IntegerField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.nombre, self.apellido)
    
class historiaClinica(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=500)
    fechaModif = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        txt = "{0}"
        return txt.format(self.paciente)
    
class turno(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    #fecha = models.CharField(max_length=30)
    #hora = models.CharField(max_length=30)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(blank=True, null=True)
    medico = models.ForeignKey(medico, on_delete=models.CASCADE)
    estado = models.CharField(max_length=30)
    def __str__(self):
        txt = "{0} Fecha:{1} Hora:{2} Medico:{3}"
        return txt.format(self.paciente, self.fecha, self.hora, self.medico ) 
    




class vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=35)
    tel = models.IntegerField()
    mail = models.EmailField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.nombre, self.apellido)
   
class lado(models.Model):
    descripcion = models.CharField(max_length=30)
    
    
    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)

class distancia(models.Model):
    descripcion = models.CharField(max_length=30)
    
    
    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)  

class marco(models.Model):
    descripcion = models.CharField(max_length=30)
    
    
    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)

class estado(models.Model):
    descripcion = models.CharField(max_length=30)
    
    
    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)
    
class pago(models.Model):
    descripcion = models.CharField(max_length=30)
    
    
    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)

class producto(models.Model):
    nombre = models.CharField(max_length=20)
    lado = models.ForeignKey(lado, on_delete=models.CASCADE)
    distancia = models.ForeignKey(distancia, on_delete=models.CASCADE)
    marco = models.ForeignKey(marco, on_delete=models.CASCADE)
    precio = models.FloatField()
    
    def __str__(self):
        txt = "{0}, LADO:{1}, DISTANCIA:{2}, MARCO/{3}"
        return txt.format(self.nombre, self.lado, self.distancia, self.marco)

    
    
class pedido(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(vendedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    pago = models.ForeignKey(pago, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    def __str__(self):
        txt = "PRODUCTO: {0}, VENDEDOR: {1}, ESTADO: {2}"
        return txt.format(self.producto, self.vendedor, self.estado)
    
    

# Create your models here.
class Todo(models.Model):
    # id is auto generated primary key
    item = models.CharField(max_length=60)
    def __str__(self):
        return self.item