from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import HeroSerializer, TodoSerializer, pacienteSerializer, medicoSerializer, historiaClinicaSerializer, turnoSerializer, vendedorSerializer, productoSerializer, pedidoSerializer, ladoSerializer, distanciaSerializer, marcoSerializer, estadoSerializer, pagoSerializer, usuarioSerializer
from .models import Hero, Todo, paciente, medico, historiaClinica, turno, vendedor, producto, pedido, lado, distancia, marco, estado, pago, usuario



# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class pacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all().order_by('id')
    serializer_class = pacienteSerializer
    
class medicoViewSet(viewsets.ModelViewSet):
    queryset = medico.objects.all().order_by('id')
    serializer_class = medicoSerializer
    
class historiaClinicaViewSet(viewsets.ModelViewSet):
    queryset = historiaClinica.objects.all().order_by('id')
    serializer_class = historiaClinicaSerializer
    
class turnoViewSet(viewsets.ModelViewSet):
    queryset = turno.objects.all().order_by('id')
    serializer_class = turnoSerializer
    
class vendedorViewSet(viewsets.ModelViewSet):
    queryset = vendedor.objects.all().order_by('id')
    serializer_class = vendedorSerializer
    
class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all().order_by('id')
    serializer_class = productoSerializer
    
class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all().order_by('id')
    serializer_class = pedidoSerializer
    
class ladoViewSet(viewsets.ModelViewSet):
    queryset = lado.objects.all().order_by('id')
    serializer_class = ladoSerializer
    
class distanciaViewSet(viewsets.ModelViewSet):
    queryset = distancia.objects.all().order_by('id')
    serializer_class = distanciaSerializer
    
class marcoViewSet(viewsets.ModelViewSet):
    queryset = marco.objects.all().order_by('id')
    serializer_class = marcoSerializer
    
class estadoViewSet(viewsets.ModelViewSet):
    queryset = estado.objects.all().order_by('id')
    serializer_class = estadoSerializer
    
class pagoViewSet(viewsets.ModelViewSet):
    queryset = pago.objects.all().order_by('id')
    serializer_class = pagoSerializer
    
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all().order_by('id')
    serializer_class = usuarioSerializer
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all().order_by('id')
#     serializer_class = TodoSerializer

# class to perform GET, POST for grabbing all todo records and adding a todo record
class TodoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Todo.objects.all().order_by('id')
        serializer = TodoSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class to perform PUT, PATCH and DELETE for updating and deleting todo records
class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    @csrf_exempt
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    # by default ZingGrid will send a /url/:id to update a whole row 
    @csrf_exempt
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # by default ZingGrid will send a /url/:id to update a single cell 
    @csrf_exempt
    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # by default ZingGrid will send a /url/:id to delete     
    @csrf_exempt
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)