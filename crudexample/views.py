from django.shortcuts import render

# define the definition/function to return our template page
def zinggrid(request):
    title = "Siguen el wampa"
    return render(request, 'zinggrid.html', {'title': title})

def vista_edicion_heroes(request):
    title = "Detalle del heroe"
    return render(request, './includes/Ver-Editar-heroes.html', {'title': title})



def pacientes(request):
    title = "pacientes"
    return render(request, 'pacientes.html', {'title': title})

def vista_edicion_pacientes(request):
    title = "Detalle del paciente"
    return render(request, './includes/pacientes-ver-agregar-modificar.html', {'title': title})




def turnos(request):
    title = "turnos"
    return render(request, 'turnos.html', {'title': title})

def vista_edicion_turnos(request):
    title = "Detalle turnos"
    return render(request, './includes/turnos-ver-agregar-modificar.html', {'title': title})



def pedidos(request):
    title = "pedidos"
    return render(request, 'pedidos.html', {'title': title})

def vista_edicion_pedidos(request):
    title = "Detalle pedidos"
    return render(request, './includes/pedidos-ver-agregar-modificar.html', {'title': title})




def login(request):
    title = "login"
    return render(request, 'login.html', {'title': title})

def menu_principal(request):
    title = "menu_principal"
    return render(request, 'menu-principal.html', {'title': title})


def historial(request):
    title = "historial"
    return render(request, 'historial.html', {'title': title})

def vista_edicion_historial(request):
    title = "Detalle historial"
    return render(request, './includes/historial-ver-agregar-modificar.html', {'title': title})







