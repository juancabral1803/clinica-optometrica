"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('vista_turnos/', views.turnos, name='turnos'),
    path('detalle_turnos/', views.vista_edicion_turnos, name='detalle_turnos'),
    path('vista_pacientes/', views.pacientes, name='pacientes'),
    path('detalle_pacientes/', views.vista_edicion_pacientes, name='detalle_pacientes'),
    path('vista_pedidos/', views.pedidos, name='pedidos'),
    path('detalle_pedidos/', views.vista_edicion_pedidos, name='detalle_pedidos'),
    path('menu_principal/', views.menu_principal, name='menu_principal'),
    path('zinggrid/', views.zinggrid, name='zinggrid'),
    path('detalle_heroes/', views.vista_edicion_heroes, name='detalle_heroes'),
    path('vista_historial/', views.historial, name='historial'),
    path('detalle_historial/', views.vista_edicion_historial, name='detalle_historial'),
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),
    path('', include('usuario.urls')),
    
    
 ]