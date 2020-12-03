# serializers.py
from rest_framework import serializers

from .models import Hero, Todo, paciente, medico, historiaClinica, turno, vendedor, producto, pedido, lado, distancia, marco, estado, pago, usuario

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        # id is auto generated primary key
        fields = ('id','name', 'alias', 'age', 'email')

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # id is auto generated primary key
        fields = ('id', 'item')
        
class pacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paciente
        # id is auto generated primary key
        fields = ('id', 'nombre_apellido', 'dni', 'domicilio', 'email', 'telefono')
        
class medicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = medico
        # id is auto generated primary key
        fields = ('id','nombre', 'apellido', 'matricula')
        
class historiaClinicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = historiaClinica
        # id is auto generated primary key
        fields = ('id','paciente', 'observacion', 'fechaModif')
        
class turnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = turno
        # id is auto generated primary key
        fields = ('id','paciente', 'fecha', 'hora', 'medico')
        
class vendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vendedor
        # id is auto generated primary key
        fields = ('id','nombre', 'apellido', 'tel', 'mail')
        
class productoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producto
        # id is auto generated primary key
        fields = ('id','nombre', 'lado', 'distancia', 'marco', 'precio')
        
class pedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pedido
        # id is auto generated primary key
        fields = ('id', 'paciente', 'vendedor', 'producto', 'estado', 'pago', 'cantidad', 'subtotal')
        
class ladoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lado
        # id is auto generated primary key
        fields = ('id','descripcion')
        
class distanciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = distancia
        # id is auto generated primary key
        fields = ('id','descripcion')
        
class marcoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marco
        # id is auto generated primary key
        fields = ('id','descripcion')
        
class estadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estado
        # id is auto generated primary key
        fields = ('id','descripcion')
        
class pagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pago
        # id is auto generated primary key
        fields = ('id','descripcion')
        
class usuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuario
        # id is auto generated primary key
        fields = ('id','nombre_usuario', 'clave', 'rol')