from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'pacientes', views.pacienteViewSet)
router.register(r'medicos', views.medicoViewSet)
router.register(r'historiaClinicas', views.historiaClinicaViewSet)
router.register(r'turnos', views.turnoViewSet)
router.register(r'vendedors', views.vendedorViewSet)
router.register(r'productos', views.productoViewSet)
router.register(r'pedidos', views.pedidoViewSet)
router.register(r'lados', views.ladoViewSet)
router.register(r'distancias', views.distanciaViewSet)
router.register(r'marcos', views.marcoViewSet)
router.register(r'estados', views.estadoViewSet)
router.register(r'pagos', views.pagoViewSet)
router.register(r'usuarios', views.usuarioViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # register todo get, post
    path('todos', views.TodoList.as_view()),
    # register todo put, patch delete
    path('todos/<int:pk>', views.TodoDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
